# FMA-Scraper
A collection of scripts to assist in scraping the FreeMusicArchive.

## Table of Contents

1. Overview
2. Installation
3. Usage
4. Future Plans

## Overview

This is a collection of scripts to aid in scraping the FMA's website for music. The first part of the scripts should be able to scrape selected genres and output the song URLs into subgenre specific documents, these will be separated by line breaks. The second part of the scripts should be able to download all subgenre songs into their releveant subgenre folders.

## Installation

*Please note these scripts have only been tested on Windows 8.1 running Python 2.7.5.*

### Prerequisites

You will require:
* Python 2 (Python 3 untested)
* Requests
* Re
* Codecs
* Os
* Sys
* Wget

Most of these modules come preinstalled with Python nowadays.

## Usage

1. Copy the script files into the folder you wish for the music to be downloaded into.
2. Ensure you have write permission in that folder.
3. Run 'FMA Scraper.py', this will create a list of download URLs for songs.
4. Run 'FMA Downloader.py', this will download any lists of songs found into their releveant folders.

## Future Plans

Future Plans include:
* Multithreaded downloads.
* Multi-genre support.
