# Linux Auth Log Analyzer

A simple Python-based tool to analyze Linux authentication logs and detect
suspicious SSH login activity such as repeated failed password attempts.

This project is intended as a learning exercise in defensive cybersecurity
and log analysis.

## What This Tool Does

- Reads Linux-style authentication logs
- Identifies failed SSH login attempts
- Extracts source IP addresses
- Flags IPs with repeated failures as potentially suspicious

This simulates how a security analyst might begin investigating
brute-force or credential-stuffing attacks.

## How to Run

1. Clone the repository
2. Ensure Python is installed
3. Run the analyzer with a log file:
   python analyzer.py sample_auth.log

## Project Scope

This is a learning-focused tool

It does not block attacks or modify system settings

Log files used are sample/simulated for safety

## What I Learned

How Linux authentication logs are structured

How brute-force SSH attacks appear in logs

Basic log parsing and pattern detection

Writing simple CLI-based security tools in Python

## Made by Srijoni Ghosh
