# write tests for parsers

from seqparser import (
        FastaParser,
        FastqParser)

import pytest


def test_freebie_parser_1():
    """
    This one is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert True # things after the assert are true statements


def test_freebie_parser_2():
    """
    This too is a freebie
    DO NOT MODIFY THIS FUNCTION
    """
    assert 1 != 2

        
def test_FastaParser():
    """
    Write your unit test for your FastaParser class here. You should generate
    an instance of your FastaParser class and assert that it properly reads in
    the example Fasta File.

    Some example of "good" test cases might be handling edge cases, like Fasta
    files that are blank or corrupted in some way. Two example Fasta files are
    provided in /tests/bad.fa and /tests/empty.fa
    """
    records = []
    with open("data/test.fa", "r") as fasta_file:
        fasta_parser = FastaParser("data/test.fa")
        for record in fasta_parser._get_record(f_obj = fasta_file):
            print(record)
            records.append(record)
    
    num_lines = len(open("data/test.fa", "r").readlines())
    
    assert len(records) == num_lines / 2
    print("NEW TEST")
    records = []
    with open("tests/bad.fa", "r") as fasta_file:
        fasta_parser = FastaParser("tests/bad.fa")
        for record in fasta_parser._get_record(f_obj = fasta_file):
            print(record)
            records.append(record)
    
    assert len(records) == 0
    print("NEW TEST")
    records = []
    with open("tests/blank.fa", "r") as fasta_file:
        fasta_parser = FastaParser("tests/blank.fa")
        for record in fasta_parser._get_record(f_obj = fasta_file):
            print(record)
            records.append(record)
    
    assert len(records) == 0



def test_FastaFormat():
    """
    Test to make sure that a fasta file is being read in if a fastq file is
    read, the first item is None
    """
    records = []
    with open("data/test.fq", "r") as fasta_file:
        fasta_parser = FastaParser("data/test.fq")
        for record in fasta_parser._get_record(f_obj = fasta_file):
            records.append(record)
    
    assert records[0][0] == None


def test_FastqParser():
    """
    Write your unit test for your FastqParser class here. You should generate
    an instance of your FastqParser class and assert that it properly reads 
    in the example Fastq File.
    """
    pass

def test_FastqFormat():
    """
    Test to make sure fastq file is being read in. If this is a fasta file, the
    first line is None
    """
    records = []
    with open("data/test.fa", "r") as fasta_file:
        fastq_parser = FastqParser("data/test.fa")
        for record in fastq_parser._get_record(f_obj = fasta_file):
            records.append(record)
    
    assert records[0][0] == None