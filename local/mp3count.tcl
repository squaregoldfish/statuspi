#!/usr/bin/tclsh

set mp3Files [glob -nocomplain "/Media/Audio/Podcasts/*/*mp3"]

set chan [open "mp3_count.txt" w]
puts $chan [llength $mp3Files]
close $chan
