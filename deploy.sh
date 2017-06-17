#!/bin/bash
# 简易记录log
echo -----begin deploy----$(date)  >> /tmp/deploy_sh.log
cd ~/www_paperweekly/ 
git pull origin
echo -----end deploy----$(date)  >> /tmp/deploy_sh.log
#top
# cd dir
# git pull
