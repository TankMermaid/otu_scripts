#!/usr/bin/env ruby
#
# author: scott w olesen <swo@mit.edu>

require 'arginine'
require 'nokogiri'

params = Arginine::parse do |a|
  desc "get top hits from blast xml"
  opt :n, desc: "number of hits to show", default: 10, cast: :to_i
  argf "blast xml"
end

doc = Nokogiri::XML(ARGF)

doc.xpath("//Iteration").each do |iter|
  # put down the sequence name
  name = iter.at_xpath("./Iteration_query-def").content
  len = iter.at_xpath("./Iteration_query-len").content.to_i

  puts name

  # look through the hits
  hits = iter.at_xpath("./Iteration_hits").xpath("./Hit")
  hits.first(10).each do |hit|
    desc = hit.at_xpath("./Hit_def").content
    acc = hit.at_xpath("./Hit_accession").content

    identity = hit.at_xpath("./Hit_hsps/Hsp/Hsp_identity").content.to_i
    pid = (identity.to_f / len * 100).round(1)

    puts [pid, desc, acc].join("\t")
  end

  puts
end