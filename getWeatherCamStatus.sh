#!/bin/bash

webcamStatus=0

wget -q -m -nd http://www.squaregoldfish.co.uk/live/webcam.jpg

timecheck=`find . -mmin -10 -name webcam.jpg`
if [ ! $timecheck ]
then
  webcamStatus=1
fi

greyPixels=`convert webcam.jpg -format %c histogram:info: |grep 808080|cut -d':' -f 1`
if [ $greyPixels -gt 10000 ]
then
  webcamStatus=1
fi

echo $webcamStatus > webcamStatus


