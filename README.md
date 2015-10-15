### kollari
A collection of tools for publishing and operating a scholarly journal

## A journal in a box

The kollari project is an effort to create a fully-featured, peer-reviewed
scholarly journal using only free software and existing, widely-available web
services. Our goal is to discover what infrastructure is necessary and 
sufficient to launch and operate a scholarly journal.

## How does this work?

Traditionally, journals have a set of guidelines for structuring and 
formatting articles for submission, leaving to the authors to obtain (often by 
purchase) the required software and to use the software correctly. Instead of
guidelines, journals built with kollari provide authors with a template 
article and all of the software required to process the template. At the cost
of some flexibility, this confers several major advantages :

* No more back-and-forth between authors and editors about formatting
* Authors, editors and reviewers can generate proofs themselves in a few seconds
* Articles are automatically formatted as PDF, HMTL, eBook, and 
  machine-parseable JSON.

The template consists of a git repository (you are looking at it) containing
an iPython notebook and a few scripts. The notebook is to be filled out with
the text, code, figures and references. The authors can run the kollari pipeline
to generate proofs as they prepare the article for submission. Errors raised by
kollari indicate problems that must be corrected before submission. When the 
article is finished and all errors are resolved, the authors create a tagged 
release on GitHub, and submit it to the journal. 

The editors of the journal then clone the tagged release. This makes it possible
to keep the review process confidential, if that is desired. The editors may then
recruit reviewers, who may then interact with the journal's clone of the 
repository by 

* Opening issues
* Submitting proposed changes in pull requests
* Submitting a review overview document in a pull request

When the editors deem it appropriate, they can allow the authors to respond to
open issues and submit pull requests. By retaining control of the in-review clone
of the article, the editors have the final say on whether to incorporate changes
from reviewers or authors and when to mark issues as resolved.

When the editors decide the review process has concluded with a satisfactory 
outcome, they make tagged release of the in-review article, and archive it using
[Zenodo](https://zenodo.org/). The kollari tools include a script for indexing all 
publications and generating a journal website using GitHub Pages.

## Name

We chose name kollari from the wasp *Andricus kollari*, which forms 
galls in oak trees. From about the 5th century to the 19th, these galls
were collected to extract gallotannic acid. Fermentation of oak galls 
with iron sulfate creates a ferrous tannate complex that is soluble in 
water. This allows it to penetrate paper, and its oxidation creates a 
pigment. This process was used for creating writing inks well into the 
20th century, when synthetic inks became widely available.

Like the wasp for which is named, kollari is both several steps removed 
from the act of writing, yet present at the moment of conjunction between 
pen and paper.
