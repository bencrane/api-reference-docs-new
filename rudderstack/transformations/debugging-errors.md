# Debugging Transformation Errors

Debug various transformation and library errors.

* * *

  * __5 minute read

  * 


This guide lists the different errors you might encounter while using transformations and libraries, and how to fix them.

## JavaScript

#### **ReferenceError**

This error occurs when a non-existent variable is referenced somewhere in the transformation.

Sample code and error| Possible solution  
---|---  
      
    
    export function transformEvent(event, metadata) {  
       event.someValue = value;   
       return event;  
    }

  
**Error** :
    
    
    “ReferenceError: value is not defined \n”  
    at transformEvent (base transformation: 2:25)

| Make sure variable is declared and available in the scope. You can also use an optional check:  

    
    
    if(value) {  
      event.someValue = value;  
    }  
  
Library code:
    
    
    // jslibsub  
    export function sub(a,b) {  
      return a-b-c;  
    }

Transformation code:
    
    
    import { sub } from ‘jslibsub’;  
      
    export function transformEvent(event, metadata) {  
      event.sub = sub(1, 2)  
      return event;  
    }

  
**Error** :
    
    
    ReferenceError: c is not defined  
      at sub (library jslibsub:2:14)  
      at transformEvent (base transformation:4:17)

| Make sure variable is declared and available in the scope.  
  
See Error message format for more context on the error message.  
  
#### **TypeError**

This error occurs when a property is read or function is called on an undefined variable.

Sample code and error| Possible solution  
---|---  
      
    
    export function transformEvent(event, metadata) {  
       event[‘val’]=event.context.traits.obj.val1;   
       return event;  
    }

  
**Error** :
    
    
    “TypeError: Cannot read properties of”  
    undefined (reading ‘val1’)\n   
    at transformEvent (base transformation:2:43)

| Use [optional chaining](<https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Optional_chaining>) when accessing nested fields.  

    
    
    event.val = event.context?.traits?.obj?.val1;  
  
#### **SyntaxError**

This error occurs when you run a syntactically invalid code, that is, it does not conform to the language syntax. For example, `SyntaxError: Unexpected identifier`, `SyntaxError: Unexpected token`.

Sample code and error| Possible solution  
---|---  
      
    
    export function transformEvent(event, metadata) {  
     returns event;   
    }

  
**Error** :
    
    
    SyntaxError: Unexpected identifier  
    [base transformation:2:13]

| Check your code for any misspelt keywords and missing operators/commas.  
  
#### **Expected…Found error**

This error occurs when you specify a transformation function other than `transformEvent` or `transformBatch`.

Sample code and error| Possible solution  
---|---  
      
    
    export function transformEvent2(event, metadata) {  
       return event;   
    }

  
**Error** :
    
    
    Error: Expected one of transformEvent,transformBatch.   
    Found

| Verify that the transformation function is either `transformEvent` or `transformBatch`.  
  
#### **Import error**

This error occurs when the module you are tring to import from a library does not exist.

Sample code and error| Possible solution  
---|---  
      
    
    import {add} from ‘jsLib’;   
    export function transformEvent(event, metadata) {  
       return event;   
    }

  
**Error** :
    
    
    Error: import from jsLib failed. Module not found.

| Verify that the module you are trying to import exists in the transformation library.  
  
## Python

#### **NameError**

This error occurs when when the transformation tries to access or use a variable that has not been defined or assigned a value.

Sample code and error| Possible solution  
---|---  
      
    
    def transformEvent(event, metadata):  
       event[‘some_value’]=value  
       return event

  
**Error** :
    
    
    NameError(“name ‘value’ is not defined”)  
      at transformEvent (base transformation: line 2)  
      event[‘some_value’]=value

| Make sure variable is declared and available in the scope. You can also use an optional check:  

    
    
    if(value):  
      event.someValue = value;  
      
  
Library code:
    
    
    def sub(a, b):  
      return a-b-c

Transformation code:
    
    
    from pylibsub import sub  
      
    def transformEvent(event, metadata):  
      event[‘sub’] = sub(1,2)  
      return event

  
**Error** :
    
    
    NameError("name ‘c’ is not defined")  
      at sub (library pylibsub: line 2)  
       return a-b-c  
      at transformEvent (base transformation: line 4)  
      event[‘sub’] = sub(1,2)

| Make sure variable is declared and available in the scope.  
  
See Error message format for more context on the error message.  
  
#### **ZeroDivisionError**

This error occurs when when the transformation attempts to divide a number by zero.

Sample code and error| Possible solution  
---|---  
      
    
    def transformEvent(event, metadata):  
       event[‘value’]=0/0  
       return event

  
**Error** :
    
    
    ZeroDivisionError(‘division by zero’)  
       at transformEvent (base transformation: line 2)  
       event[‘val’]=0/0

| Verify your transformation logic.  
  
#### **KeyError**

This error occurs when the transformation attempts to access a dictionary item that does not exist.

Sample code and error| Possible solution  
---|---  
      
    
    def transformEvent(event, metadata):  
       event[‘val’]=event[‘context’][’traits’][‘obj’][‘val1’]  
       return event

  
**Error** :
    
    
    KeyError(‘obj’)  
       at transformEvent (base transformation: line 2)  
       event[‘val’]=event [‘context’][’traits’][‘obj’][‘val1’]

| Verify the key that transformation is attempting to access exists in the dictionary. You can also set a optional chaining event like:  

    
    
    event[‘val’] = event.get(‘context’).get(  
    ‘traits’,{}).get(‘obj’, {}).get(‘val1’)  
  
#### **BadCodeError**

This error occurs when the transformation contains syntactically invalid code or is trying to import an unsupported module/package.

Sample code and error| Possible solution  
---|---  
      
    
    def transformEvent(event, metadata):  
       returns event

  
**Error** :
    
    
    BadCodeError(‘invalid syntax (, line 2)’)

| Verify the syntax of your transformation code.  
      
    
    from pyLib2 import add  
    def transformEvent(event, metadata):  
       return event

  
**Error** :
    
    
    BadCodeError(“Unpermitted import(s). Supported modules /  
    packages for import: {‘sampleTransformationLibrary’,  
    ‘time’, ‘random’, ‘base64’, ‘string’, ‘dateutil’,  
    ‘hashlib’, ‘uuid’, ‘urllib’, ’re’, ‘rudderEmail’,  
    ‘json’, ‘collections’, ‘datetime’, ‘ast’, ‘requests’,  
    ‘math’, ‘user_transformation’, ‘hmac’}”)

| Verify that the library imports one of the supported built-in packages and user-written libraries only.  
  
#### **Exception error**

This error occurs when you specify a transformation function other than `transformEvent` or `transformBatch`.

Sample code and error| Possible solution  
---|---  
      
    
    def transformEvent2(event, metadata):  
       return event

  
**Error** :
    
    
    Exception(“Expected one of [’transformEvent’, ’transformBatch’].  
    Found []”)

| Verify that the transformation function is either `transformEvent` or `transformBatch`.  
  
#### **ImportError**

This error occurs when the module you are tring to import from a library does not exist or is not found.

Sample code and error| Possible solution  
---|---  
      
    
    from pyLib1 import adds  
    def transformEvent(event, metadata):  
       return event

  
**Error** :
    
    
    ImportError(“cannot import name ‘adds’   
    from ‘pyLib1’ <redacted_path_to_pyLib1>”)

| Verify that the module you are trying to import exists in the transformation library.  
  
## Error message format

#### **Standalone transformation**

A typical JavaScript transformation error is shown:
    
    
    ReferenceError: c is not defined
        at sub (library jssublib:2:14)
        at transformEvent (base transformation:4:22)
    

You can interpret the above error as follows:

  * `ReferenceError: c is not defined`: The actual error message.
  * `at sub (library jssublib:2:14)`: Module in which the error occurs (`line: position`).
  * `at transformEvent (base transformation:4:22)`: Depicts where the module is referenced in the transformation (`line: position`).


#### **Transformation referencing a library**

A typical Python transformation error is shown:
    
    
    NameError(\"name 'c' is not defined\")
        at sub (library pylibsub: line 2)
        return a-b-c
        at transformEvent (base transformation: line 4)
        event['sub'] = sub(1,2)
    

You can interpret the above error as follows:

  * `NameError("name 'c' is not defined")`: The actual error message.
  * `at sub (library pylibsub: line 2)`: Line at which error occurred in the library.
  * `return a-b-c`: Line where the error occurred.
  * `at transformEvent (base transformation: line 4)`: Line at which library is referenced by the base transformation.
  * `event['sub'] = sub(1,2)`: Line where `lib` function is called.