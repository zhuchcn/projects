#!/home/chhzhu/programs/miniconda3/bin/python

from Bio.SeqIO.QualityIO import FastqGeneralIterator
from Bio.Seq import Seq
from Bio import SeqUtils
import os

class pairedEndReadsFilterGroup(object):
    def __init__(self, forward_list, reverse_list, input_path, output_path, barcodes_file, forward_primer, reverse_primer):
        self.forward_list = []
        with open(forward_list) as fh:
            for line in fh:
                self.forward_list.append(line.strip())

        self.reverse_list = []
        with open(reverse_list) as rh:
            for line in rh:
                self.reverse_list.append(line.strip())

        self.input_path = input_path
        self.output_path = output_path
        
        self.barcodes = dict()
        with open(barcodes_file) as bh:
            for line in bh:
                if not line.startswith('#'):
                    line = line.strip()
                    key, val = line.split('\t',1)
                    self.barcodes[key] = val

        self.forward_primer = forward_primer
        self.reverse_primer = reverse_primer

    def filtByPrimerGroup(self):
        for forward, reverse in zip(self.forward_list, self.reverse_list):
            input_forward = self.input_path + '/' + forward + '.fastq'
            input_reverse = self.input_path + '/' + reverse + '.fastq'
            output_forward = self.output_path + '/' + forward + '.filt.fastq'
            output_reverse = self.output_path + '/' + reverse + '.filt.fastq'
            fwd_primer = self.barcodes[forward.split('_')[0]] + self.forward_primer
            rvs_primer = self.reverse_primer
            
            print('Now processing sample' + forward +' and ' + reverse)
            pe = pairedEndReadsFilter(input_forward, input_reverse, output_forward, output_reverse)
            pe.filtByPrimer(fwd_primer, rvs_primer)
            


class pairedEndReadsFilter(object):
    def __init__(self, input_forward, input_reverse, output_forward, output_reverse):
        self.input_forward = input_forward
        self.input_reverse = input_reverse
        self.output_forward = output_forward
        self.output_reverse = output_reverse

    def filtByPrimer(self, fwd_primer, rvs_primer):
        with open(self.input_forward) as fh:
            with open(self.input_reverse) as rh:
                
                count_keep = 0
                count_discard = 0

                for ((title_f, seq_f, qual_f),(title_r, seq_r, qual_r)) in zip(FastqGeneralIterator(fh), FastqGeneralIterator(rh)):
                    
                    try:
                        if (SeqUtils.nt_search(seq_f, fwd_primer)[1] == 0) & (SeqUtils.nt_search(seq_r, rvs_primer)[1] == 0):
                            with open(self.output_forward, 'a') as ofh:
                                ofh.write('@' + '\n'.join([title_f, seq_f, '+', qual_f]) + '\n')
                            with open(self.output_reverse, 'a') as orh:
                                orh.write('@' + '\n'.join([title_r, seq_r, '+', qual_r]) + '\n')
                            count_keep += 1
                        else:
                            count_discard += 1
                    except IndexError:
                        count_discard += 1
        print('     Number of reads saved: ' + str(count_keep))
        print('     Number of reads discard :' + str(count_discard))

def getopts(argv):
    opts = {}
    while argv:
        if argv[0][0] == '-':
            opts[argv[0]] = argv[1]
        argv = argv[1:]
    return(opts)

if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)
    pe = pairedEndReadsFilterGroup(myargs['--input-forward-list'],
                                   myargs['--input-reverse-list'],
                                   myargs['--input-path'],
                                   myargs['--output-path'],
                                   myargs['--barcodes'],
                                   myargs['--forward-primer'],
                                   myargs['--reverse-primer'])
    pe.filtByPrimerGroup()

