#!/usr/bin/bash
#https://cloud.google.com/blog/topics/developers-practitioners/cloud-storage-file-system-vertex-ai-workbench-notebooks/
#https://cloud.google.com/storage/docs/cloud-storage-fuse/cli-options

export EXE_GCSFUSE="/usr/bin/gcsfuse";
export GCS_BUCKET="usfs-gcp-rand-test3-data-usc1";
export GCS_MOUNT_POINT="/home/jupyter/projects/gcs";

cd ~/ # This should take you to /home/jupyter/

#is the mount point present?
if [ ! -d "${GCS_MOUNT_POINT}" ];
then
    # Create a folder that will be used as a mount point
    status=$( mkdir -p "${GCS_MOUNT_POINT}" );

    #was the directory creation successful?
    if [ "${status}" != "0" ];
    then
      echo "ERROR: Status of ${status} returned.  Investigate attempts to create the (${GCS_MOUNT_POINT}) directory.";
    fi
fi

#mount the file system
status=$( gcsfuse --implicit-dirs --rename-dir-limit=100 --max-conns-per-host=100 "${GCS_BUCKET}" "${GCS_MOUNT_POINT}" );
#status=$( ${EXE_GCSFUSE} "${GCS_BUCKET}" "${GCS_MOUNT_POINT}" );
if [ "${status}" != 0 ];
then
    echo "ERROR: Status of:";
    echo " ${status}";
    echo "returned.  Investigate attempts to gcsfuse the (${GCS_MOUNT_POINT}) directory.";
else
    echo "SUCCESS: Mounted ${GCS_MOUNT_POINT} for all buckets within this projects.";
fi

#ls "${GCS_MOUNT_POINT}"
