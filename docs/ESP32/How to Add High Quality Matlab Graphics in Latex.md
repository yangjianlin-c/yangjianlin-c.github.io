Date: 2014-09-14
Title: How to Add High Quality Matlab Graphics in Latex
intro: Many user may would like to include high quality Matlab graphics in their Latex articles or books. Here I will share some tips how to do it. From easy to difficult, I will introduce three methods. 
Tags: Latex Matlab
Status: public


Many user may would like to include high quality Matlab graphics in their Latex articles or books. Here I will share some tips how to do it. From easy to difficult, I will introduce three methods:

1. Export an .eps file from Maltab, and include it in Latex article.
2. Export an .eps file from Maltab, edit this file with Adobe Illustrator, then use it in Latex.
3. Produce a TikZ code from the Matlab figure, and then include the TikZ code in Latex.

Now I will detail introduce each method, at last will talk about each method advantage and disadvantage.

## 1.Export .eps file

This is the most easy way, just need save the figure in Matlab as an .eps file, and then include the .eps file in Latex.

Or with Matlab command:

```matlab
saveas(gcf,'Plot1.eps', 'psc2')
```

Or it can use below command to print the figure to .eps file:

```matlab
set(gcf, 'PaperPositionMode', 'auto');
print -depsc2 Plot1.eps
```

Then you can include the .eps file in Latex, for example:

```latex
\documentclass{article}
\usepackage{graphicx}
\begin{document}    
\begin{figure}[h]
\centerline{\includegraphics[width=8cm]{Plot1.eps}}
\caption{This is Plot1}
\end{figure}
\end{document}
```

Although this method is very easy, but the texts or vibration characters font on the figure may not same as Latex. And the text size will depend on the export file size, and the figure size setting in Latex. It may be very hard to control the characters size on figures comply with the article text size.

## 2. Edit .eps file in AI

As said above, the text on Matlab figure maybe not the same style as the text in Latex, and it hard to choose a suitable size for the final figure. But we can edit the .eps file with Adobe Illustrator before use it. Here I will introduce some tips about it.

1. First, open the .eps file, and **set the document size** same as your document size in Latex. For example, if I will product a A4 paper article, then I set the size as A4.
2. **Scale the figure** in AI, the size is what you wanted it would be in A4 paper.
3. **Set the text size** as it real size. For example, the article text size is 12pt, while I want the text on figure is a little smaller than it, set it 10.5pt.
4. Also you can **edit** the line style, color, weight, etc in AI. It’s very easy to edit any element in AI.
![figure size](https://lh4.googleusercontent.com/-xN-pNScUfrg/UpbF5AsdvGI/AAAAAAAAKa4/gOYhPTWw7Yo/s0/size.png "size.png")

By this way we can control the figure size and text size very well.

## 3. Export Matlab figure as TikZ code
You will find edit .eps file in AI will be very powerful to edit the figure, but if there are lots of pictures, it will need a lot of time. And AI is a commercial program. There is another way to produce a high quality pictures, by using TikZ.

If you are familiar with Latex, you should know `TikZ`. We can insert TikZ code in Latex document directly, and it will produce the pictures we need. But it need spend sometime to learn TikZ. More info and examples can be found [here](www.texample.net/tikz/).

Here is a solution, that can export Matlab figure as TikZ code with `matlab2tikz`, download it [here](http://www.mathworks.com/matlabcentral/fileexchange/22022).

matlab2tikz supports the conversion of most MATLAB figures, including 2D and 3D plots. For plots constructed with third- party packages, your mileage may vary.

The workflow is as follows:

1. Place the matlab2tikz scripts (contents of src/ folder) in a directory where MATLAB can find it (the current directory, for example).

2. Generate your plot in MATLAB.

3. Invoke matlab2tikz by
```matlab
>> matlab2tikz();
```
   or
```matlab
>> matlab2tikz('myfile.tex');
```
  The script accepts numerous options; check them out by invoking the help,
```matlab
>> help matlab2tikz
```
Sometimes, MATLAB makes it hard to create matching LaTeX plots by keeping
invisible objects around or stretches the plots too far beyond the bounding box.
Use
```matlab
>> cleanfigure;
>> matlab2tikz('myfile.tex');
```
to first clean the figure of unwanted entities, and then convert it to TeX.

4. Add the contents of `myfile.tex` into your LaTeX source code; a
   convenient way of doing so is to use `\input{/path/to/myfile.tex}`.
   Also make sure that at the header of your document the Pgfplots package
   is included:
```latex
\documentclass{article}
\usepackage{pgfplots}
% and optionally (as of Pgfplots 1.3):
\pgfplotsset{compat=newest}
\pgfplotsset{plot coordinates/math parser=false}
\newlength\figureheight
\newlength\figurewidth
\begin{document}
\input{myfile.tex}
\end{document}
```

Amazing, right?

If you experience bugs, have nice examples of what matlab2tikz can do, or if you are just looking for more information, please visit the web page of matlab2tikz [https://github.com/nschloe/matlab2tikz](https://github.com/nschloe/matlab2tikz). 

In conclude, in this post I introduced 3 methods about how to insert Matlab figure into Latex.

1.  Save as .eps file, is most easy and quickly. But if you need very strict requirement for the figure text, size, line style, it will not satisfy you.
2. Edit the .eps file in AI. It’s powerful edit any element in AI. If you just write an article, it will be good enough. But if you have a lot of picture, you must spend a lot of time to edit each picture. 
3. Export Matlab figure to TikZ code. Sometimes it will be efficient, and it’s free. But you need spend time to learn TikZ, and sometimes the convert will not work as you wanted.