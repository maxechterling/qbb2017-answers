## hifive analysis
hifive 5c-complete express data/Nora_primers.bed -C data/Nora_ESC_male_E14.counts -P nora
## create heatmaps
hifive 5c-heatmap nora.fcp nora_frag.heat -i nora_frag.png -F npz -a compact -b 0 -d fragment
hifive 5c-heatmap nora.fcp nora_enr.heat -i nora_enr.png -F npz -a compact -b 0 -d enrichment
## get top interacting CTCF sites
./ctcf_ixns.py data/ctcf_peaks.tsv data/Nora_Primers.bed > top_ctcf_ixns.txt