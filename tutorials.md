## [QIIME2](docs.qiime2.org/)

+ Qiime2 is actively under developing, with new version released every other month. By the time that I wrote this, qiime2's DADA2 function is much slower (plus there is some problem that we haven't solved of using qiime2's dada2). However, qiime2 is embedded with the fasttree tool. So if you want to use it to build a phylogenic tree, please read the tutorial in qiime2 website, and make sure to use the latest version.

## [DADA2 Tutorial](https://benjjneb.github.io/dada2/tutorial.html)

+ The original dada2 is a R package available on bioconductor.

## [PICRUSt Tutorial with de novo Variants](https://github.com/LangilleLab/microbiome_helper/wiki/PICRUSt-Tutorial-with-de-novo-Variants)

+ This tutorial allows you to use dada2 output to do function prediction with PICRUSt.

## [Phyloseq](http://joey711.github.io/phyloseq/)

+ Phyloseq is a package that dedicated for microbiome data analysis. It can calculate the alpha diversity, and beta diversity with different methods (unifrac, bray curtis, etc.). But it does not have a phylogenic tree building method which is required by the unifrac method. So you will need to use the qiime2 before phyloseq. The phyloseq's plotting functions are very capsulized, and not very flexible. 
