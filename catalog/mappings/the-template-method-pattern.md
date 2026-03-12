---
slug: the-template-method-pattern
name: "The Template Method Pattern"
kind: archetype
source_frame: publishing
target_frame: object-oriented-design
categories:
  - software-engineering
author: agent:metaphorex-miner
contributors: []
related:
  - the-strategy-pattern
  - the-factory-pattern
---

## What It Brings

A template is a document with blanks -- a form letter with spaces for
the name and date, a stencil with cutouts for paint, a page layout
with placeholders for content. The GoF Template Method pattern maps
this onto software: a base class defines the skeleton of an algorithm
with certain steps left as abstract methods that subclasses fill in.
The publishing metaphor frames inheritance as a printing process: the
template is fixed, and each edition supplies its own content for the
variable slots.

Key structural parallels:

- **The template defines structure; content varies** -- a form letter
  establishes the greeting, body paragraphs, and closing. Each
  recipient gets the same structure with personalized details. The
  pattern's base class defines the algorithmic skeleton (the order of
  steps, the control flow), while subclasses provide specific
  implementations for individual steps. The metaphor makes the
  fixed/variable distinction feel natural: of course a template has
  blanks.
- **You fill in the blanks; you don't redesign the form** -- a tax
  form has specific fields. You can enter your numbers, but you can't
  rearrange the sections or add new ones. The pattern constrains
  subclasses similarly: they implement the abstract steps but cannot
  change the order or overall flow. The metaphor frames this constraint
  as proper use of a template rather than a limitation.
- **Templates are reused across many editions** -- one newsletter
  template serves hundreds of issues. One base class serves many
  subclasses. The metaphor captures the pattern's economics: design
  the structure once, instantiate it many times with different content.
- **The template creator controls the experience** -- the designer of
  a form decides what information matters, in what order, and what's
  optional. The base class author decides which steps are mandatory,
  which are overridable, and which are hook methods with default
  behavior. The metaphor frames the base class author as an editor
  or designer with authority over the document's shape.
- **Templates enforce consistency** -- every issue of a magazine has
  the same layout even though the articles differ. Every subclass
  follows the same algorithmic structure even though the step
  implementations differ. The metaphor frames uniformity as a feature
  (brand consistency) rather than rigidity.

## Where It Breaks

- **Templates in publishing are filled in by users; Template Methods
  are filled in by programmers** -- a form letter's blanks are
  completed at runtime by a human with specific information. The
  pattern's "blanks" are completed at compile time by a programmer
  writing a subclass. The metaphor conflates runtime personalization
  with compile-time specialization. The document metaphor suggests
  flexibility that the inheritance mechanism doesn't actually provide
  at runtime.
- **Publishing templates are passive; Template Methods contain
  executable logic** -- a page layout doesn't do anything. A template
  method actively calls the abstract steps in sequence, manages control
  flow, and may contain substantial logic between the variable steps.
  The metaphor undersells the base class: it's not a blank form, it's
  a program with holes.
- **Stencils are additive; Template Methods are substitutive** -- a
  stencil adds paint through cutouts onto a surface. The pattern
  requires subclasses to replace abstract method bodies wholesale.
  The physical metaphor of filling in blanks suggests insertion, but
  the mechanism is actually method overriding -- replacement, not
  addition.
- **The metaphor hides the inversion of control** -- in normal
  publishing, the author drives the process: they decide when to write
  each section. In the Template Method pattern, the base class drives:
  it calls the subclass methods when it chooses. This "Hollywood
  Principle" (don't call us, we'll call you) is the pattern's most
  important structural feature, and the publishing metaphor completely
  obscures it. A template sitting on a desk doesn't call anyone.
- **"Template" suggests data; "Method" suggests behavior** -- the
  compound name pulls in two directions. "Template" evokes a static
  document; "Method" evokes executable code. The tension between these
  source domains reflects a real conceptual difficulty: the pattern
  is simultaneously a structure and a process. Neither the publishing
  nor the programming metaphor alone captures this duality.
- **Real templates can be ignored; Template Methods enforce
  compliance** -- you can leave form fields blank, write outside the
  margins, or throw the template away. The pattern's abstract methods
  must be implemented. The metaphor imports optional compliance where
  the pattern enforces mandatory participation.

## Expressions

- "Fill in the blanks" -- implementing abstract methods, the template
  metaphor at its most direct
- "Hook method" -- an optional step with a default implementation,
  mixing fishing with publishing metaphors
- "The template defines the skeleton" -- the architectural metaphor
  layered on top of the publishing one
- "Don't call us, we'll call you" -- the Hollywood Principle,
  abandoning the publishing metaphor entirely for show business
- "Override the step" -- subclass customization, using a dominance
  metaphor (override) rather than a publishing one (fill in)
- "Template method vs. strategy" -- the canonical comparison,
  inheritance-based templates versus composition-based strategies

## Origin Story

The concept of algorithmic templates predates the GoF book. Frameworks
in the 1980s -- particularly application frameworks in Smalltalk and
early C++ -- relied heavily on base classes that defined processing
skeletons with overridable steps. The GoF formalized this as the
Template Method pattern in 1994, choosing a name that borrows from
publishing rather than manufacturing or architecture. "Template"
emphasizes the fixed structure with variable content, which is
arguably the clearest metaphor in the GoF catalog for its intended
concept. The name has become somewhat ironic in modern development:
C++ templates, template engines (Mustache, Jinja), and HTML templates
all use the word "template" for different concepts, creating
terminological confusion that the original publishing metaphor didn't
anticipate.

## References

- Gamma, E. et al. *Design Patterns: Elements of Reusable Object-
  Oriented Software* (1994), Chapter 5: Behavioral Patterns
- Johnson, R.E. & Foote, B. "Designing Reusable Classes" (1988) --
  early articulation of the framework design principles that underlie
  the Template Method pattern
- Sweet, R.E. "The Mesa Programming Environment" (1985) -- early use
  of template methods in system programming frameworks
