General comments:
  # use "Nektar++" throughout, not "Nektar" - Nektar is actually the precursor to Nektar++ and is a very different beast...
  
  # dont make figure captions too concise! e.g. something like "Figure 3.4: Representation of the Force parameter in the TemPSS tree illustrating the representation of the XML-encoded properties ofoptionality and repeatability."

  # make sure all code snippets are in a monospace font

  # there are a few grammatical / spelling errors in the text, particularly in the later chapters, so make sure to have a read through

  # can I propose compiling a list of the supported Nektar++ parameters for the Appendix, with their path in the TemPSS tree and any properties such as optionality, repeatability, etc? Maybe split up by the main branches. I think this would be a useful reference for someone wishing to extend the TemPSS tree in the future.
  
  # conclusions can be quite concise. Summarise what has been achieved, with reference to the objectives.


Specific comments:
  Intro: The primary aim of the Nektar++ libraries is to encapsulate the spectral/hp element method, upon which various PDE solvers for simulating different physical phenomena can be built.

  Intro: "rich text-editors" -> "Graphical User Interfaces" (e.g. your OpenFOAM example!)
  
  Aim: Be specific: graphical/web-based interface, allows user to specify problem to solve in an intuitive manner, generates a syntactically valid XML free from logical errors (prevents selection of incompatible  unctionality, rather than a simulation which is necessarily numerically stable, for example).
  
  Objective 1: functionality and parameter space
  
  Objectives: "functions" -> "simulation parameters"? Does it make sense to call the Reynolds number a "function"?
  
  P5 XML Structure: multiply -> multiple
  
  Figure 3.2: Only some of these boxes ever seem to be discussed in the text? Not clear what you mean by "TemPSS file dependency" (see general comment above on figure captions!). Where does the populated profile fit in to this?
  
  I think you need to give a more general summary of how XSLT transforms work. You have bits of XML which are written to the output file verbatim, then you have the <xsl...> tags which perform the actual processing. You have these bite-size chunks of templates which get substituted in when certain criteria are met (i.e. the name and mode).
  
  Feel free to use inline code (formatted as monospace) to be more precise, e.g. "During transformation the <xsl:if ...> tag performs a test...", "The <xsl:apply-template> evaluates and substitutes the template which matches the given 'select' and 'mode'".
  
  P8: "line 41, of figure 3.8", but lines go from 1-6.
  
  P10: "illucidate" -> "elicudate".
  
  Problem Specification: Discuss geometry loading, BC generation etc? I seemed to remember you improved an aspect of this? You should write what you did.

  Fig 3.11: These look rather basic and do not show off the full scope of the parameter space they encapsulate! They are also not referenced in the text. Consider removing, and reference a full list of parameters in the Appendix?
  
  Eq 4.4: We typically use \mathbf{u} for the overall flow, \mathbf{U} for the base flow and \mathbf{u'} for the perturbation, so this should probably be: \mathbf{u} = \mathbf{U} + \epsilon\mathbf{u'}

  Eq 4.5: \mathbf{u} -> \mathbf{U}, also \nabla\cdot\mathbf{u'} = 0
  
  Eq 4.6: same as above, specifically say "steady linearised N-S"...
  
  "Unsteady Navier-Stokes"  this is the base case and repeats Eq 4.1? Maybe just add this subtitle after "4.1.4..."
  
  Test cases: possibly the specific tables of parameters are not necessary and could be put in the appendix? The plots of forces, etc, are maybe a unnecessarily large? If you have time, it might be worth setting these to run for a longer FinalTime to show that the results are truly identical to the non-TemPSS case.

