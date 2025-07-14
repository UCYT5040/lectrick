# Lectrick

Lectrick is an esoteric programming language that makes characters do things.

## Primer

Lectrick uses a monospace font internally (similar to that of your code editor).

Lectrick considers the shape and colors of characters.

Below is a list of "actions." Each action has a specific shape (some have colors too).

Consider the `HORIZONTAL WIRE` action below. The shape is a horizontal line. A couple characters that resemble this
shape include the hyphen `-`, then en dash `–`, and the em dash `—`. Other characters also may exist that resemble this
shape, and they will work too!

Electricity is measured in LE.

### Backwards Compatibility

Lectrick’s character recognition assigns the action that each character most closely resembles.

That means that if a new action is added, and this action more closely resembles a character than the previous action,
the character will now perform the new action.

Thus, before updating, you should generate an action map with the `map` command. After updating, generate another action
map, and compare the two maps to see if any characters have changed actions.

### Character Width

Some characters are wider than others. Lectrick does not account for this. You must ensure that the characters you use
form a perfect grid. The `map` command can help you visualize this.

Another tool is the `watch` command. In Jetbrains IDEs, the editor allows for variable width characters, but the
terminal does not. So, if you use the `watch` command, you can see how Lectrick interprets the characters from the
terminal while you edit the file in the editor.

### Fire

Careful! If you connect two sources of power together, they will set on fire, causing an error!

Check out one-way actions to prevent this.

## Sample Programs

### `programs/hello`

Outputs `hello`.

![Program with annotations explaining how it works](programs/hello.png)

## Actions

### What do these images mean?

These images are generated from sample characters that resemble the action. These sample characters are not the only
characters that will work with the action.

Think about what characters resemble the shape you see in the image, and try them out!

#### These images look weird!

The characters are stretched to fit the shape. This is to account for similar characters that have different widths or
heights.

### HORIZONTAL WIRE

![HORIZONTAL WIRE](shapes/HORIZONTAL%20WIRE.svg)

Electricity flows horizontally.

### VERTICAL WIRE

![VERTICAL WIRE](shapes/VERTICAL%20WIRE.svg)

Electricity flows vertically.

### CROSS WIRE

![CROSS WIRE](shapes/CROSS%20WIRE.svg)

Electricity input in one direction flows out the other three directions, split evenly.

### POWER SOURCE

![POWER SOURCE](shapes/POWER%20SOURCE.svg)

Electricity flows out in all directions. 255 LE is split evenly between the four directions.

### LIGHT BLOCK

![LIGHT BLOCK](shapes/LIGHT%20BLOCK.svg)

When electricity flows into a light block, a character is printed. The character is determined by the amount of LE.

### ONE WAY LEFT/RIGHT

Restricts flow in one direction.

If flow is currently being restricted, the excess power will be output vertically or discarded.

This can act as a form of error handling, as colliding power results in a fire.

#### ONE WAY LEFT

![ONE WAY LEFT](shapes/ONE%20WAY%20LEFT.svg)

#### ONE WAY RIGHT

![ONE WAY RIGHT](shapes/ONE%20WAY%20RIGHT.svg)

### SPLIT/DOUBLE

![SPLIT](shapes/SPLIT.svg)

Any electricity flowing into a split will be divided or multiplied by 2.

This does not split/double the electricity evenly between outputs: it just performs the operation mathematically and
outputs the result in all three directions.

#### SPLIT

![SPLIT](shapes/SPLIT.svg)

#### DOUBLE

![DOUBLE](shapes/DOUBLE.svg)

### INCREMENT/DECREMENT

Increase or decrease the amount of electricity recieved, and broadcast the new value in the 3 other directions.

If the value goes below 0 or above 255, it will be overflow, wrapping around to 255 or 0 respectively.

#### INCREMENT

![INCREMENT](shapes/INCREMENT.svg)

#### DECREMENT

![DECREMENT](shapes/DECREMENT.svg)

## Commands

Before running, make sure you have `uv` installed. If you have Python, grab it with:

```bash
pip install uv
```

### Run

```bash
uv run lectrick run <file>
```

Add `--visualize` to visualize the program as it runs. You’ll probably want to adjust the size of tile names with
`--visualize-width <n>` (default is 10). Then you’ll want to add a pause with `--pause <seconds>`.

For the visualization to work well, your terminal should support ANSI escape codes. Yellow tiles are currently dealing
with electricity, red tiles have received electricity (will handle next turn), and the rest are not currently handling
electricity.

Note that `--pause` pauses 3 times per turn.

### Map

Generate a map of the actions in a file. This is useful to visualize the actions and characters in a file.

```bash
uv run lectrick map <file>
```

### Lookup

Check what action matches a character:

```bash
uv run lectrick lookup "<character>"
```

Add the `--generate-overlays` flag to generate images in the `overlays` directory. This is useful to visualize why a
character is not working as expected.

### Reverse Lookup

Check what characters match an action:

```bash
uv run lectrick reverse-lookup "<action>"
```

Use the `--char-range <range>` to specify a range of characters to search through (like `--char-range 32-126` for all
printable characters or `--char-range 1000` for the first 1000 characters).

`--min-strength <strength>` can be used to specify a minimum strength for the action. This is useful for actions that
have a lot of similar characters.

### Generate Shapes

This command generates shapes for each tile. It is neccessary for the comparison of characters to actions, and it also
generates the SVGs used in the documentation.

```bash
uv run lectrick generate-shapes
```

### CHR/ORD

Convert between characters and their ordinal values.

```bash
uv run lectrick chr <ordinal>
uv run lectrick ord <character>
```

### Watch

Watch a file for changes and print it’s contents.

Note: This command does not actually run the program.

```bash
uv run lectrick watch <file>
```
