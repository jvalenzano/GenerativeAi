#!/usr/bin/bash
#
years=( $(seq 2020 2024) )

echo "Categories"
for year in ${years[@]}
do
    echo "Processing Categories for ${year}"
    source_filename="./CARA_${year}.txt"
    target_filename="./CARA_${year}_category.txt"
    if [ -f "${source_filename}" ];
    then
	    cat ${source_filename} | cut -d'^' -f1,2,5 > ${target_filename}
	    data_rows=$(wc -l ${source_filename});
	    echo "${year} - ${data_rows} added to the output file.";
    else
        echo "Failed to create category output file for ${year}, inspect your output."
    fi
done
data_rows=$(wc -l *_category.txt);
echo "${data_rows} total records."

echo ""
edcho "Comments"
for year in ${years[@]}
do
    echo "Processing Comments for ${year}"
    source_filename="./CARA_${year}.txt"
    target_filename="./CARA_${year}_comment.txt"
    #if [ -f "${source_filename}" ];
    #then
    #    cat ${source_filename} | cut -d'^' -f1,2,3 > ${target_filename}
    #    data_rows=$(wc -l ${source_filename});
    #    echo "${year} - ${data_rows} added to the output file.";
    #else
    #    echo "Failed to create comment output file for ${year}, inspect your output."
    #fi
done
data_rows=$(wc -l *_comment.txt);
echo "${data_rows} total records."

echo ""
echo "Coded Comments"
for year in ${years[@]}
do
    echo "Processing Coded (sub-parsed) Comments for ${year}"
    source_filename="./CARA_${year}.txt"
    target_filename="./CARA_${year}_coded.txt"
    #if [ -f "${source_filename}" ];
    #then
    #    cat ${source_filename} | cut -d'^' -f1,2,4 > ${target_filename}
    #    data_rows=$(wc -l ${source_filename});
    #    echo "${year} - ${data_rows} added to the output file.";
    #else
    #else
    #    echo "Failed to create coded comment output file for ${year}, inspect your output."
    #fi
done
data_rows=$(wc -l *_coded.txt);
echo "${data_rows} total records."
