#!/usr/bin/env ruby
#
# author: scott w olesen <swo@mit.edu>
#
# leave off the sequence at the beginning of each line. replace it with seq1, seq2, etc.

require 'arginine'

params = Arginine::parse do 
  desc "replace actual sequences with seq\#"
  arg :table, :desc => "output counts table"
  arg :fasta, :desc => "output fasta"
  argf "seq table"
end

open(params[:table], 'w') do |table|
  open(params[:fasta], 'w') do |fasta|
    ARGF.each do |line|
      if $. == 1
        table.write(line)
      else
        # find the sequence
        seq = line.match(/^[A-Z]+/)[0]
        seq_n = $. - 1
        seq_name = "seq#{seq_n}"
        table.write(line.sub(seq, seq_name))
        fasta.write(">#{seq_name}\n#{seq}\n")
      end
    end
  end
end