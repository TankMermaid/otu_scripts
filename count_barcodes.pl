#!/usr/bin/env perl

use warnings;
use strict;
use 5.10.1;

my %counts = ();

while (<>) {
    next unless $. % 4 == 1;

    chomp;
    s/^.*#//;
    s/..$//;

    if (exists $counts{$_}) {
        $counts{$_} += 1;
    } else {
        $counts{$_} = 1;
    }
}

my @codes = sort { $counts{$b} <=> $counts{$a} } keys %counts;

for my $code (@codes) {
    print $code . "\t" . $counts{$code} . "\n";
}

__END__
