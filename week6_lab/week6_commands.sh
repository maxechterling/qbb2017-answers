## build chromosome 19 index
bowtie2-build chr19.fa chr19_ind

## align reads
bowtie2 -x genomes/chr19_ind fastqs/CTCF_G1E.fastq -S CTCF_G1E.sam
bowtie2 -x genomes/chr19_ind fastqs/CTCF_ER4.fastq -S CTCF_ER4.sam
bowtie2 -x genomes/chr19_ind fastqs/input_ER4.fastq -S input_ER4.sam
bowtie2 -x genomes/chr19_ind fastqs/input_G1E.fastq -S input_G1E.sam

## call peaks
macs2 callpeak -t ./sams/CTCF_G1E.sam -c ./sams/input_G1E.sam -g 61431566 -n G1E
macs2 callpeak -t ./sams/CTCF_ER4.sam -c ./sams/input_ER4.sam -g 61431566 -n ER4

## find lost peaks (G1E --> ER4)
bedtools intersect -a ./peaks/G1E_peaks.narrowPeak -b ./peaks/ER4_peaks.narrowPeak -v > diff_lost.bed
## find gained peaks (G1E --> ER4)
bedtools intersect -a ./peaks/ER4_peaks.narrowPeak -b ./peaks/G1E_peaks.narrowPeak -v > diff_gained.bed

## Sort top results
sort -k 7 -n -r peaks/ER4_peaks.narrowPeak > top.narrowPeak

## get motif sequences
bedtools getfasta -fi genomes/chr19.fa -bed top_ER4_peaks.narrowPeak > top_ER4.fa

## actual meme
/usr/local/opt/meme/bin/meme-chip -db motif_databases/JASPAR/JASPAR_CORE_2016_vertebrates.meme -meme-maxw 20 top_ER4.fa 