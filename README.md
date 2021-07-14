# Initialization Time Extensible Metadata
A remedy for a multitude of data ailments.

## Interoperability of Data
Where is the future of data from Minority report where information can move effortlessly between systems and still 
retain its context and value?

Why do data scientists spend 80% of their time conforming data?

Why can't my doctor take advantage of the wealth of health information gathered by my wearables and 
[consumer medical instruments](https://www.alivecor.com/kardiamobile/)?

The information we collect and move around doesn't include the information needed to ingest it. Mostly because the 
instructions for consuming the data are outside the process.

The advantages of interoperability at application levels is now well recognized. It is time to establish the 
interoperability of our information.

html, json, encoding

What about lineage, governance, security?

## ITEMic as a proof of concept
This repo is an experiment to show whether we can successfully embed enough metadata with inforamtion as it flows
through a system, to allow that system to make better decisions at run-time.

itemic.py contains a class definition which is intended to be used with multiple inheritance for objects which also contain information fields.
itemic_handler.py contains a class definition which is intended to be used with multiple inheritance for objects which will handle itemic objects.
For example, 
Inheriting from the Itemic class will provide a framework to store information in a consistent way to be consumed  

### Security tags
#### Confidentiality
How important is it to prevent unauthorized disclosure? 
#### Integrity
How important is it to prevent data corruption?
How long is the data considered relevant or authoritative?
#### Availability
How important is it to ensure timely access or prevent untimely destruction?
#### Authentication
What kind of authentication is required to consume or alter? 
#### Authorization
How are authenticated consumers connected to permissions? 
#### Audit
How has the information been consumed or altered?

### Lineage tags
Where did this information originate? How many systems has it passed through?

### Governance tags
How long should the data be retained?
Is it subject to a hold?
Is its use subject to approval?
For what purposes can we use it?
What destinations can it be sent to?

## POC Schema
Hierarchical collection of name/value pairs organized into nodes. All leaves must be name/value pairs.
Top level nodes:
* Security
  * Confidentiality: One of [Public, Internal, Confidential, Restricted]
  * Integrity: True/False
  * Availability: One of [High, Med, Low]
* Lineage: a list of tuples:
  * Source
  * Destination
  * Timestamp
* Governance
  * Retention Date: date/time after which it should be purged
  * Hold Date: date/time after which legal hold is released
  * Business purpose: list of business functions for which it can be used e.g. [Marketing, Resale, Market Research]
### Security
