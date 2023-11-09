# YAML in Markdown Format

## Scalars
A scalar represents a single value, such as a string, number, boolean, or null.

**String:**
```yaml
name: John Doe
```

**Integer:**
```yaml
age: 35
```

**Float:**
```yaml
height: 5.9
```

**Boolean:**
```yaml
is_student: false
```

**Null:**
```yaml
nickname: null
```

## Lists
Lists are sequences of items that can include scalars, maps, or other lists.

**Simple List:**
```yaml
items:
  - Apple
  - Banana
  - Cherry
```

**List of Dictionaries:**
```yaml
users:
  - name: John Doe
    age: 35
  - name: Jane Smith
    age: 28
```

**Nested Lists:**
```yaml
ingredients:
  - - Flour
    - Water
  - - Strawberries
    - Sugar
```

## Associative Arrays (Dictionaries or Maps)
Associative arrays are key-value pair collections, also known as dictionaries or maps.

**Simple Dictionary:**
```yaml
address:
  street: 123 Apple St.
  city: New York
  postal_code: 12345
```

**Nested Dictionary:**
```yaml
database:
  host: localhost
  port: 5432
  credentials:
    username: dbuser
    password: securepassword
```

## Complex Structures
YAML can represent complex structures through a combination of lists and maps.

**Complex Example:**
```yaml
- job: Developer
  skills:
    - name: Python
      experience: '3 years'
    - name: JavaScript
      experience: '2 years'
- job: Writer
  skills:
    - name: Copywriting
      experience: '5 years'
    - name: SEO
      experience: '3 years'
```

## Multi-Line Strings
YAML supports multi-line strings without complicated escaping, offering a very readable format.

**Literal Block Scalar (`|`):**
```yaml
description: |
  This is a description
  that spans multiple lines
  without any special formatting.
```

**Folded Block Scalar (`>`):**
```yaml
description: >
  This is a folded style description
  that spans multiple lines, but it
  will be rendered as a single line
  with spaces where newlines were.
```
