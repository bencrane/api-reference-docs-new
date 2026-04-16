# Enigma Console File Exchange Documentation

> https://documentation.enigma.com/console/file-exchange

## Overview

The File Exchange feature enables bidirectional data transfer between your systems and Enigma. Organizations can "upload data files for batch enrichment, matching, or processing" and receive results delivered to connected storage.

## Key Constraint

File paths within connected sources cannot exceed 110 characters, measured from the bucket or SFTP directory root.

## Three Connection Options

| Type | Use Case |
|------|----------|
| Enigma SFTP | Quick setup with Enigma-managed infrastructure |
| Your SFTP | Existing SFTP servers under your control |
| Your S3 | AWS workflows and large-scale operations |

## Setup Process

Users navigate to **Settings > Account > Data Connections**, select **Connect New Source**, choose their source type, and provide a nickname for the connection.

## Enigma SFTP Details

After setup, Enigma provides connection details including hostname and username. Configuration requires an SSH public key for authentication and optionally a PGP public key for file encryption.

## Your SFTP Server

This option requires an internet-accessible SFTP server with credentials. Users specify the host, username, and password, plus optional read/write folder paths and PGP encryption settings.

## Your S3 Bucket

S3 authentication supports either access keys or IAM roles. The IAM role approach is recommended as it uses temporary credentials rather than long-term keys. Users must grant Enigma specific S3 permissions including ListBucket, GetObject, PutObject, and DeleteObject actions.

## File Encryption

Optional PGP encryption protects files before delivery, operating alongside existing transport-layer security (TLS for S3, SSH for SFTP).
