# ant

.ant is a raster image file format.

## header

to make it easier to recognize by both user and computer, specific byte is present,\
`[61]`, `a` in ascii.

width and height of an image are 1-based values defined by 2 bytes, width and height,\
`[w][h]`, therefore max size of the file format is 256px x 256px.

## data

each pixel is a byte, meaning that the number of possible colors is 256.

the orient of matrix should be row-major,
could be redefined by the image viewing program.

color palette is defined by the image viewing program,
but ansi 256 is recommended.

## example

```
; header
61
03 01 ; 4x2
; data
01 23 45 67
89 ab cd ef
```
