# Private labeling Lob

If you are a company that is building and selling software solutions, you may want to consider leveraging Lob’s direct mail or address verification capabilities to unlock additional value, which can be repackaged and resold as part of your broader offering to your own customers.

In such cases, while there are many ways to integrate with our platform as a backend, the following are some best practices we highly recommend you follow.

{% hint style="info" %}
Interested in private labeling Lob? Reach out to[ partners@lob.com](mailto:partners@lob.com)
{% endhint %}

## Billing

Your standard Lob invoice will be a single invoice, broken out into two categories: Subscription (annual) and Usage (monthly). Our resellers often have a need to further segment their usage by different cost centers within their broader organization, in a way that's more reflective of their business operations (e.g. by use case, teams, states, or customer groups). There are two ways to achieve this:

### If you have less than 10 cost centers

If you are an Enterprise customer, you may request to [modify your invoice](https://help.lob.com/account-management/billing-and-invoices#modifying-your-invoicing-structure-7) to differentiate your monthly usage between various cost centers. Engage your CSM to receive separate invoices.&#x20;

### If you have over 10 cost centers

Another way to segment usage is to attribute your campaign mailings to the responsible cost centers within your organization, so you may accurately keep track during end-of-month reconciliation processes. We recommend using [metadata](https://help.lob.com/developer-docs/use-case-guides/mass-deletion-setup#use-lob-metadata) along with page count where applicable.

* **Postcards/self-mailers**: When submitting a request to create the mailpiece, include a metadata tag with a key for identifying your billing recipient (e.g., `customer_id` or `institution_id`), and insert a value accordingly. This way, you can filter for all the mailings sent by that particular customer or institution later and bill accordingly.<br>
* **Letters/checks**: Since the number of pages sent in a campaign may vary and therefore the cost, you will need a way to calculate the final price. Below is a sample (Python) script for how to pull a list of letters by metadata, *and* parse out the number of pages each.

```python
'''
USAGE: python3 pdf_page_count.py

This file will go and fetch mail from the LIST endpoints and basically fetch the letters, load 
them into memory and count the # of pages, Spitting out a CSV with the summary.
'''

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import resolve1
from io import BytesIO
import pandas as pd
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
import multiprocessing
from functools import partial
import numpy as np
import requests
import json
import sys

def retry_session(retries, session=None, backoff_factor=1):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=[500, 502, 503, 504, 429],
        allowed_methods=['GET']
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session

def parse_pdf(item_list):
    result_csv = pd.DataFrame(columns=['id','page_count','double_sided'])
    session = retry_session(retries=5)
    for item in item_list:
        id = item['id']
        print(id)
        r = session.get(f"{item['url']}")
        if r.status_code in (200,204,202):  
            f = BytesIO(r.content)
            f = PDFParser(f)
            document = PDFDocument(f)
            # This will give you the count of pages
            result_csv = result_csv.append({'id' : id, 'page_count' : resolve1(document.catalog['Pages'])['Count'], 'double_sided' : item['double_sided']}, ignore_index=True)

    return result_csv

def parse_data(api_key):
    url = f"https://api.lob.com/v1/letters"
    creative_url = url
    #TODO: add in any filtering you see fit (metadata, extra services, etc)
    params = {'send_date[gte]' : '2021-10-01', 'send_date[lte]' : '2021-10-12' }
    params['limit'] = '100'

    session = retry_session(retries=5)
    r = session.get(url, auth=requests.auth.HTTPBasicAuth(api_key, ''), params=params)
    j = r.json()
    # print(j)
    results = pd.DataFrame(columns=['id','page_count','double_sided'])

    results = parallelize_data(results, j['data'])

    url = j['next_url']

    #Run through the pagination
    if url is not None:
        while url is not None:
            r = session.get(url, auth=requests.auth.HTTPBasicAuth(api_key, ''))
            j = r.json()
            results = pd.concat([results,parallelize_data(results, j['data'])], ignore_index=True)
            url = j['next_url']

    results.to_csv('results_pdf_parse.csv', index=False)

def parallelize_data(results, data_list):
    num_cores = int(multiprocessing.cpu_count() - 1)  #leave one free to not freeze machine
    num_partitions = num_cores * 2 #number of partitions to split dataframe
    df_split = np.array_split(data_list, num_partitions)
    pool = multiprocessing.Pool(4)
    func = partial(parse_pdf)
    results = pd.concat(pool.map(func, df_split))
    pool.close()
    pool.join()
    return results

if __name__ == '__main__':
    ##Get API Key
    api_key = input('Enter in your API key (use your live API key to delete live resources): ')

    ##Delete
    parse_data(api_key)y
```

Now that you can identify who is sending mail and the total cost of mailpieces sent by each of your customers, you’re ready to bill them accurately.

Learn more about[ utilizing metadata tags](https://help.lob.com/print-and-mail/building-a-mail-strategy/managing-mail-settings/using-metadata) to segment your mailings.

## Try before you buy

In the world of direct mail, there are guidelines and specifications that must be followed to ensure the quality of mailpieces submitted. This is why the auditing process is so important. Your customers will likely want to see the mailpieces they’re submitting before any purchases are made. Lob enables this by providing a test environment along with ways to preview mailpieces:

### Use the test environment

With your Lob account, you have access to both a live environment (in which mailpieces will be printed and sent) and a test environment, where you can try our API and view digital proofs without needing to cancel any mailpieces from being delivered. For more information, see [Test vs Live Environments](https://help.lob.com/account-management/api-keys#test-vs-live-environment-keys-2).

{% hint style="warning" %}
We recommend that you use the Test environment to create digital proofs which you can then surface back to your customers before submitting Live.
{% endhint %}

### Preview mailpieces

We provide two ways to preview a mailpiece via each form factor’s endpoint. `GET`(Retrieve) can provide the details of an existing mailpiece (postcard request and response example [here](https://docs.lob.com/#tag/Postcards/operation/postcard_retrieve)).

1. The `url` parameter provides a full-scale digital proof of the mailpiece in PDF format. The address block on this proof is a rendered mockup, and therefore, the IMB barcode will not reflect the actual barcode printed when the piece is mailed. It is recommended to use this proof for the final sign-off on the printed mail piece.

<figure><img src="https://lh6.googleusercontent.com/OgWBrTXCIW3x3wA0C9t0yJ_UmQ3BOlT9UU26o1Q3qyBHG--xB02TeoxvXu4z7ULgCCQGIaaDA9nE3D5Y86stLbEuFZE1WvwerJCYH8NPZLe0r5Sobvc0Wd01upJIvAB4byqFIEomSTvptQxACsSK3m68cCa2RwIMb-FH724YHXlSneariEZoRBNnq1RN" alt=""><figcaption></figcaption></figure>

&#x20;  2\.  The `thumbnail` parameter provides smaller depictions of the mailpiece in PNG format, generated in small, medium, or large sizes. Due to differences in optimization and print preflight, these thumbnails may differ from the full-scale digital proof in certain circumstances. Thumbnails are considered a preview and do not necessarily reflect the final rendering of the mail piece.<br>

<figure><img src="https://lh3.googleusercontent.com/96j2t-fv2Xzxr8s5G8qCHAw852XWDFN_pbBzoPkRLJuJUCnyH0I9nqsBxr4o3YTUIJkr62zbOnBtM4WrqzEHri2lDLVqiS1FhRZ5pIXUot6Klu9er3IAK3xLuUsw1V95MHzO5ckQFUamNREMaSSZpfY9hV6HicFFyDP4CDUUzj3R8PrMFEg630rOh_nD" alt=""><figcaption></figcaption></figure>

## Give insight into the delivery process

Lob provides visibility of every step of the mail delivery process with [mail tracking events](https://help.lob.com/print-and-mail/getting-data-and-results/tracking-your-mail), for example “in transit” or “processed for delivery.” In turn, we highly recommend you surface these tracking events back to your end-customers so they can be in the loop as well.

* `GET` (Retrieve) can provide the details of an existing mailpiece (postcard `GET` request and response example [here](https://docs.lob.com/#tag/Postcards/operation/postcard_retrieve)); the `tracking_events` parameter can be used:<br>

<figure><img src="https://lh3.googleusercontent.com/qEPfN3375-aYtdW_fAvVEnRf7cLMnNCRz10CT-nQFTy4fhaRMe_lRBSJIYKVGAZehs8ARUDL3zfLCP-bzAn6WZxwcZWMCVbdPCP1z6HmpG9VgrlMTa3l7mFwPpCyx2r2APDg35EaGgew565hj0r0StLEpnG8Dmw3ROkEZcACOlDZsIDT8uYWIyX5-2tp2Q" alt=""><figcaption></figcaption></figure>

* &#x20;[Webhook notifications](https://help.lob.com/print-and-mail/getting-data-and-results/using-webhooks) can also be set up to receive and store tracking events in real-time.

<figure><img src="https://1775164782-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FiXDYGxBp6aAwhpEhTMNC%2Fuploads%2FH8fNyBkuvdEcqg5Lvm3k%2FScreen%20Shot%202022-12-16%20at%205.56.55%20PM.png?alt=media&#x26;token=4425998d-167f-4873-ad8d-68b75b590fcb" alt=""><figcaption><p>Webhook notifications can provide granular visibility into each stage of the mail delivery process, from when the order is submitted to when it arrives to the recipients' doorstep.</p></figcaption></figure>