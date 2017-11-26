#!/bin/bash
cd /Media/Audio/Podcasts;du -sm .|sed 's/\t.*//' > mp3_size.txt

