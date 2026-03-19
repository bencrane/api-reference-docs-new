# Asset URLs

All asset URLs returned by the Lob API (postcards, letters, thumbnails, etc) are signed links served over HTTPS. All links returned will expire in 30 days to prevent mis-sharing. Each time a GET request is initiated, a new signed URL will be generated.