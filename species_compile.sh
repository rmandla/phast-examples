#!/bin/bash
# look through all .maf.gz files in a directory and output all lines for the specified genomes into a new file in the directory uproot.

for i in *.gz; do
	[ -f "$i" ] || break
	echo "$i"
	pigz -cd "$i" | python species_sample.py | pigz > stn"$i"
done
