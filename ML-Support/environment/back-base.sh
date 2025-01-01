#!/usr/bin/env bash

#Most secure cross platform method
#sudo $(which conda) env export --no-builds  --name machine_learning_gpu > ./archless_environment.yml;

#conda deactivate;
#conda env update -f whatever.yml --prune;
#conda activate my_environment_name; # Must be AFTER the conda env update line!
#Reference: https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#updating-an-environment


#>>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
export the_conda="conda";
__conda_setup="$('/opt/${the_conda}/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"

if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/opt/${the_conda}/etc/profile.d/conda.sh" ]; then
        . "/opt/${the_conda}/etc/profile.d/conda.sh"
    else
        export PATH="/opt/${the_conda}/bin:$PATH"
    fi
fi
unset __conda_setup
#<<< conda initialize <<<

export exe_conda="/opt/${the_conda}/bin/conda";
export version_conda=$($exe_conda --version);

echo "Anaconda location: ${exe_conda}";
echo " Anaconda version: ${version_conda}";

the_repos=( base );
for repo in ${the_repos[@]}
do
    echo "Processing ${repo}...";
    echo "......conda env export --name ${repo} > ./${repo}.yml";
    #Most generic method
    conda env export --name "${repo}" > "./${repo}.yml";
    status=$?
    if [ "${status}" -ne 0 ];
    then
        echo "........FAILURE";
	echo "........conda env export --name ${repo} failed with status code of (${status}).";
    else
        echo "........SUCCESS";
    fi
done

#create generic requirements file
echo "Copy of pip/python System libs to requirements file.";
pip list --format=freeze > ./requirements.txt
echo "Copy of pip/python User libs to requirements file.";
pip list --format=freeze --user > ./user_requirements.txt
