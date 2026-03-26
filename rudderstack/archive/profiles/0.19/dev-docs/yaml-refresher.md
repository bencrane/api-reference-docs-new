# YAML Best Practices

> ![danger](/docs/images/warning.svg)
> 
> You are viewing documentation for an older version.
> 
> [Click here to view the latest documentation.](</docs/profiles/overview>)

# YAML Best Practices

Quick overview of YAML basics for Profiles use.

* * *

  * __4 minute read

  * 


YAML is the preferred choice for writing Profile Builder files due to its simplicity and ease of use.

This guide explains the base concepts, syntax, and best practices for writing code in YAML.

## What is YAML?

[YAML](<https://yaml.org>), short for **YAML Ain’t Markup Language** or **Yet Another Markup Language** , is a data serialization format often used in config files and exchange of data. A YAML file uses indentation, specific characters, and line breaks for representing various data structures.

## Sample YAML file

Below is how a sample YAML document looks like. It contains key-value pairs where the keys are on the left, followed by a colon (`:`), and the associated values are on the right. The hierarchy and data structure is defined using indentation. The next section explains this in more detail.
    
    
    # This is a comment
    person:
      name: Ruddy Buddy # Note the spacing used for indentation
      age: 42
      is_employed: true
      address: # An object called address
        street: Jefferson Davis Highway
        city: Ruther Glen
        state: Vermont
        phone: 555-90-210
      favorite_sports: # A list
        - soccer
        - baseball
    

The above code has details of an object called `person` with properties like `name`, `age`, `gender`, `is_student`, `address` and `favorite sports`.

Here’s how the same YAML file looks in the JSON format:
    
    
    {
      "person": {
        "name": "Ruddy Buddy",
        "age": 42,
        "is_employed": true,
        "address": {
          "street": "Jefferson Davis Highway",
          "city": "Ruther Glen",
          "state": "Vermont",
          "phone": "555-90-210"
        },
        "favorite_sports": [
          "soccer",
          "baseball"
        ]
      }
    }
    

## Indentation

In YAML, the indentation is done using spaces - to define the structure of data. Throughout the YAML file, the number of spacing should be consistent. Typically, we use two spaces for indentation. YAML is whitespace-sensitive, so do not mix spaces and tabs.
    
    
    # Example of correct indentation
    person:
      name: Ruddy Buddy # We used 2 spaces
      age: 42
    
    # Example of incorrect indentation
    person:
      name: Ruddy Buddy 
        age: 42 # We mixed spacing and tabs
    

## Comments

As shown above, YAML has single-line comments that start with hash (`#`) symbol, for providing additional explanation or context in the code. Comments are used to improve readability and they do not affect the code’s functionality.
    
    
    # YAML comment
    person:
      name: Ruddy Buddy # Name of the person
      age: 42 # Age of the person
    

## Data types in YAML

YAML supports several data types:

  * **Scalars** : Represent strings, numbers, and boolean values.
  * **Sequences** : Represent lists and are denoted using a hyphen (`-`).
  * **Mappings** : Key-value pairs used to define objects or dictionaries using colon (`:`).


    
    
    # Example of data types in YAML
    person:
      name: Ruddy Buddy # Scalar (string)
      age: 42 # Scalar (number)
      is_employed: true # Scalar (boolean)
      address: # Mapping (object)
        street: Jefferson Davis Highway
        city: Ruther Glen
        state: Vermont
        phone: 555-90-210
      favorite_sports: # Sequence (list)
        - soccer
        - baseball
    

## Chomp modifiers

YAML provides two chomp modifiers for handling line breaks in scalar values.

  * `>`: Removes all newlines and replaces them with spaces.


    
    
    description: >
      Here is an example of long description
      which has multiple lines. Later, it
      will be converted into a single line.  
    

  * `|`: Preserves line breaks and spaces.


    
    
    description: |
      Here is another long description, however
      it will preserve newlines and so the original
      format shall be as-it-is.  
    

## Special characters

You can use escape symbols for special characters in YAML. For example, writing an apostrophe in description can cause the YAML parser to fail. In this case, you can use the escape character.

## Best practices

Follow these best practices for writing clean YAML code in your Profiles projects:

  * Always keep consistent indentation (preferably spaces over tabs).
  * Give meaningful names to your keys.
  * Avoid excessive nesting.
  * YAML is case sensitive, so be mindful of that.
  * Add comments wherever required.
  * Use blank lines to separate sections like ID stitcher, feature view, etc.
  * If your strings contain special characters, then use escape symbols.
  * Make sure you end the quotes in strings to avoid errors.
  * Use chomp modifiers for multi-line SQL.


## References

  * [YAML for VS Code](<https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml>): Extension for comprehensive YAML support in Visual Studio Code.
  * [YAML Lint](<https://www.yamllint.com>) for linting.


  * [![](/docs/images/previous.svg)Previous](</docs/archive/profiles/0.19/dev-docs/commands/>)
  * [Next ![](/docs/images/next.svg)](</docs/archive/profiles/0.19/management/>)