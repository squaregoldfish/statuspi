#!/usr/bin/tclsh

set mp3Files [glob -nocomplain "*/*mp3"]

set timeTotal 0

foreach mp3File $mp3Files {
    set mp3Length [exec mp3info -p \"%S\" $mp3File]
    set timeTotal [expr $timeTotal + $mp3Length]
}

set hours [expr $timeTotal / 3600]
set minutes [expr $timeTotal / 60]

set chan [open "mp3_length.txt" w]
puts $chan $hours
close $chan

set chan [open "mp3_length_m.txt" w]
puts $chan $minutes
close $chan

