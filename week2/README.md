# herp-interns/week2
Week 2: The Central Dogma (Replication, Transcription, Translation), Mutation  

## Tuesday, Nov 1
- Wrap up Candy tree activity & evolution discussion
- Computer setup!
- Python Review! Variables, Functions, Loops, Lists, Dictionaries, Strings 
- Discussion: What is DNA? Structure/Function? Nucleotides and complimentary bases 
- Python exercise: Pair programming. Complement a strand of DNA & count bases. 
- Discussion: What is transcription? What is translation?
- Python exercise: Pair programming. Transcription and Translation 
- Discussion: Nonsynonymous vs synonymous mutations
- Python exercise: Mutations

#### Computer setup

##### Initial setup
- Make sure you are logged into your GitHub account. FORK this git repo by clicking the "Fork" button in the top right corner. This will create a copy of the repository on your own account that you can add, commit, and push your own changes to.
- CLONE your version of the repository onto your computer. Do this by navigating to the repository through YOUR Github profile. When you click on your copy of the repository, there should be a green button on the right that says "Clone or Download". Copy the URL it gives you (It should be something like: `https://github.com/YOUR-USERNAME/herp-interns.git`). Open up a terminal and use `pwd` to make sure you are in your home directory. Then, execute the command `git clone URL`. You should see this folder in your home directory if you open your Finder.
- To make sure you can receive the additions and changes I make to the repo (i.e. adding stuff into the folders for the next few weeks), you must set an UPSTREAM REMOTE. Do this by going into your Terminal, navigating to the `herp-interns` directory (remember `cd`!) and typing the command `git remote add upstream https://github.com/carosee/herp-interns.git`.
- Verify that you have done this correctly by typing the command `git remote -v`. You should see something like this:

```shell
$ git remote -v
origin  https://github.com/your-username/herp-interns.git (fetch)
origin  https://github.com/your-username/herp-interns.git (push)
upstream  https://github.com/carosee/herp-interns.git (fetch)
upstream  https://github.com/carosee/herp-interns.git (push)
```
- See also: https://help.github.com/articles/configuring-a-remote-for-a-fork/

##### General git tips
- Recall: To add changes to your github, use the command `git add FILENAME` (You may use a * in place of FILENAME to add all the changes you've made)
- To commit changes, use the command `git commit -m "YOUR MESSAGE HERE"`.
- To push your changes to github, use the command `git push origin master`.
- Every week I will push changes to the remote repository with code files and other things we will need for the week. At the beginning of each class, you will need to download these changes into your own forked repo by executing the following commands:
```shell
$ git fetch upstream
$ git checkout master
$ git merge upstream/master
```
- See also: https://help.github.com/articles/syncing-a-fork/

#### Python review
- See pythonreview.md.  

#### DNA coding exercise
- In pairs, fill in the functions `complement()` and `count_bases()` in `substitutions.py`.
- Create a test case for each other's functions (how to make a test case?) and make sure your functions are correct.
- Given a sample sequence, count the number of each base in the sequence and compare it to the number of each base in the complement. What do you notice, and why is this the case?

#### Transcription and Translation coding exercise
- In pairs, fill in the functions `transcribe_dna()`, and `translate_rna()` in `substitutions.py`.
- Create a test case for each other's functions (how to make a test case?) and make sure your functions are correct.
- Test the functions using the beta globin gene sequences. Find the mutation. Does the resulting protein change?  

#### Mutation coding exercise
  + Fill in the functions `random_substitution()`, `is_synonymous()`, and `count_synonymous` in `substitutions.py`.  
  + Why don't all DNA mutations change the protein sequence?  
  

## Thursday, Nov 3
- Finish up whatever didn't get done on Tuesday
- Discussion: Heredity & Probability
- Evolution in relation to allele frequencies, mutations
- What is selection? What is drift?
- More python review. Install anaconda and intro to Numpy!
  
