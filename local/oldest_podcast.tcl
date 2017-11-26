#!/usr/bin/tclsh

set fileList [glob -nocomplain "/Media/Audio/Podcasts/*/*"]

set oldest 0
set oldest_file ""
set today [clock seconds]

foreach podcast $fileList {
  if {[string first "mp3" $podcast] > -1} {
    set fileDate [file mtime $podcast]
    set age [expr ($today - $fileDate) / 86400]
    if {$age > $oldest} {
      set oldest $age
      set oldest_file $podcast
    }
  }
}

set chan [open "oldest_podcast.txt" w]
puts $chan $oldest
close $chan

set chan [open "oldest_podcast_name.txt" w]
puts $chan $oldest_file
close $chan

