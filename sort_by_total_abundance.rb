#!/usr/bin/env ruby
#
# author: scott w olesen <swo@mit.edu>

require 'arginine'

params = Arginine::parse do 
  desc "sort rows based on sum of all the entries in that row"
  flag :index, :desc => "ignore first column?"
  flag :header, :desc => "ignore first row?"
  argf "table"
end

header = ''
lines = []
ARGF.each do |line|
  if $. == 1 and params[:header]
    # this is the header line, just save it
    header = line.chomp
  else
    # for other lines, store the sum of the numeric fields
    fields = line.split
    idx = fields.shift if params[:index]
    sum = fields.map(&:to_f).inject { |s, x| s + x }

    # only keep the line if it's nonzero
    lines << [sum, line]
  end
end

# print out the lines in order
puts header if params[:header]
puts lines.sort { |a, b| b.first <=> a.first }.map(&:last)