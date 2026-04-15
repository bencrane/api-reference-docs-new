# Region selection

Modal allows you to specify the cloud region a Function runs in.

This may be useful if:

you are required (for regulatory reasons or by your customers) to process data within certain regions.
you want to reduce egress fees that result from reading data from a dependency like S3.
you have a latency-sensitive app where app endpoints need to run near an external DB.

Note that regardless of what region your Function runs in, all Function inputs and outputs go through Modal’s control plane in us-east-1.

Specifying a region 

To run your Modal Function in a specific region, pass a region= argument to the function decorator.

@app.function(region=["us-east"])
def f():
    import os

    print(f"running in {os.environ['MODAL_REGION']}") # us-east-1, us-east-2, us-ashburn-1, etc.
Pricing 

A multiplier on top of our base usage pricing will be applied to any Function that has a cloud region defined.

Region	Multiplier
Any region in US/EU/UK/AP	1.25x
Any region in CA/SA/ME/MX/AF	2.5x

Here’s an example: let’s say you have a Function that uses 1 T4, 1 CPU core, and 1GB memory. You’ve specified that the function should run in us-east-2. The cost to run this function for 1 hour would be ((T4 hourly cost) + (CPU hourly cost for one core) + (Memory hourly cost for one GB)) * 1.25.

If you specify multiple regions and they span the two categories above, we will apply the smaller of the two multipliers.

Region options 

Modal offers varying levels of granularity for regions. Use broader regions when possible, as this increases the pool of available resources your Function can be assigned to, which improves cold-start time and availability.

United States (“us”) 

Use region="us" to select any region in the United States.

     Broad            Specific                       Description
=====================================================================
  "us-east"           "us-east-1"                    AWS Virginia
                      "us-east-2"                    AWS Ohio
                      "us-east1"                     GCP South Carolina
                      "us-east4"                     GCP Virginia
                      "us-east5"                     GCP Ohio
                      "us-ashburn-1"                 OCI Virginia
                      "eastus"                       AZR Virginia
                      "eastus2"                      AZR Virginia
---------------------------------------------------------------------
  "us-central"        "us-central1"                  GCP Iowa
                      "us-chicago-1"                 OCI Chicago
                      "us-phoenix-1"                 OCI Phoenix
                      "centralus"                    AZR Iowa
                      "northcentralus"               AZR Illinois
                      "southcentralus"               AZR Texas
                      "westcentralus"                AZR Wyoming
---------------------------------------------------------------------
  "us-south"          "us-south1"                    GCP Dallas
---------------------------------------------------------------------
  "us-west"           "us-west-1"                    AWS California
                      "us-west-2"                    AWS Oregon
                      "us-west1"                     GCP Oregon
                      "us-west2"                     GCP Los Angeles
                      "us-west3"                     GCP Salt Lake City
                      "us-west4"                     GCP Las Vegas
                      "us-sanjose-1"                 OCI San Jose
                      "westus"                       AZR California
                      "westus2"                      AZR Washington
                      "westus3"                      AZR Arizona
European Economic Area (“eu”) 

Use region="eu" to select any region in the European Economic Area (EEA). Notably, this does not include the UK.

     Broad            Specific                       Description
=====================================================================
  "eu-west"           "eu-central-1"                 AWS Frankfurt
                      "eu-west-1"                    AWS Ireland
                      "eu-west-3"                    AWS Paris
                      "europe-west1"                 GCP Belgium
                      "europe-west3"                 GCP Frankfurt
                      "europe-west4"                 GCP Netherlands
                      "eu-frankfurt-1"               OCI Frankfurt
                      "eu-paris-1"                   OCI Paris
                      "westeurope"                   AZR Netherlands
                      "germanywestcentral"           AZR Frankfurt
                      "francecentral"                AZR Paris
                      "polandcentral"                AZR Warsaw
---------------------------------------------------------------------
  "eu-north"          "eu-north-1"                   AWS Stockholm
                      "northeurope"                  AZR Ireland
                      "swedencentral"                AZR Sweden
                      "norwayeast"                   AZR Oslo
---------------------------------------------------------------------
  "eu-south"          "eu-south-1"                   AWS Milan
                      "eu-south-2"                   AWS Spain
                      "italynorth"                   AZR Milan
                      "spaincentral"                 AZR Madrid
Asia–Pacific (“ap”) 

Use region="ap" to select any region in Asia–Pacific.

     Broad            Specific                       Description
=====================================================================
  "ap-northeast"      "ap-northeast-1"               AWS Tokyo
                      "ap-northeast-2"               AWS Seoul
                      "ap-northeast-3"               AWS Osaka
                      "asia-east1"                   GCP Taiwan
                      "asia-northeast1"              GCP Tokyo
                      "asia-northeast3"              GCP Seoul
                      "koreacentral"                 AZR Seoul
                      "japaneast"                    AZR Tokyo
                      "japanwest"                    AZR Osaka
---------------------------------------------------------------------
  "ap-southeast"      "ap-southeast-3"               AWS Jakarta
                      "asia-southeast1"              GCP Singapore
                      "southeastasia"                AZR Singapore
                      "malaysiawest"                 AZR Kuala Lumpur
---------------------------------------------------------------------
  "ap-south"          "ap-south-1"                   AWS Mumbai
                      "asia-south1"                  GCP Mumbai
                      "asia-south2"                  GCP Delhi
                      "centralindia"                 AZR Pune
                      "westindia"                    AZR Mumbai
                      "southindia"                   AZR Chennai
---------------------------------------------------------------------
  "ap-melbourne"      "ap-melbourne-1"               OCI Melbourne
---------------------------------------------------------------------
                      "australia-southeast1"         GCP Sydney
                      "ap-sydney-1"                  OCI Sydney
                      "australiaeast"                AZR Sydney
United Kingdom (“uk”) 

Use region="uk" to select any region in the United Kingdom.

     Broad            Specific                       Description
=====================================================================
  "uk"                "eu-west-2"                    AWS London
                      "europe-west2"                 GCP London
                      "uk-london-1"                  OCI London
                      "uksouth"                      AZR London
                      "ukwest"                       AZR Cardiff
Canada (“ca”) 

Use region="ca" to select any region in Canada.

     Broad            Specific                       Description
=====================================================================
  "ca"                "ca-central-1"                 AWS Montreal
                      "northamerica-northeast2"      GCP Toronto
                      "ca-toronto-1"                 OCI Toronto
                      "ca-montreal-1"                OCI Montreal
                      "canadacentral"                AZR Toronto
                      "canadaeast"                   AZR Quebec
Middle East (“me”) 

Use region="me" to select any region in the Middle East.

     Broad            Specific                       Description
=====================================================================
  "me"                "me-west1"                     GCP Tel Aviv
                      "uaenorth"                     AZR Dubai
                      "qatarcentral"                 AZR Doha
South America (“sa”) 

Use region="sa" to select any region in South America.

     Broad            Specific                       Description
=====================================================================
  "sa"                "sa-east-1"                    AWS São Paulo
                      "southamerica-east1"           GCP São Paulo
                      "brazilsouth"                  AZR São Paulo
Africa (“af”) 

Use region="af" to select any region in Africa.

     Broad            Specific                       Description
=====================================================================
  "af"                "southafricanorth"             AZR Johannesburg
Mexico (“mx”) 

Use region="mx" to select any region in Mexico.

     Broad            Specific                       Description
=====================================================================
  "mx"                "mexicocentral"                AZR Mexico
Region aliases 

The following are convenience aliases for selecting specific countries within broader geographic regions (e.g., Japan or Australia within Asia-Pacific).

     Alias            Specific                       Description
=====================================================================
  "jp"                "ap-northeast-1"               AWS Tokyo
                      "ap-northeast-3"               AWS Osaka
                      "asia-northeast1"              GCP Tokyo
                      "japaneast"                    AZR Tokyo
                      "japanwest"                    AZR Osaka
---------------------------------------------------------------------
  "au"                "australia-southeast1"         GCP Sydney
                      "ap-sydney-1"                  OCI Sydney
                      "ap-melbourne-1"               OCI Melbourne
                      "australiaeast"                AZR Sydney
