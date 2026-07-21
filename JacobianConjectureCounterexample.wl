(* ::Package:: *)

(* Jacobian Conjecture Counterexample \[LongDash] Alpoge, July 20 2026 *)
(* Interactive isosurface visualization *)


(* The map F: C^3 -> C^3 *)
F1[x_, y_, z_] := (1 + x y)^3 z + y^2 (1 + x y)(4 + 3 x y);
F2[x_, y_, z_] := y + 3 x (1 + x y)^2 z + 3 x y^2 (4 + 3 x y);
F3[x_, y_, z_] := 2 x - 3 x^2 y - x^3 z;


(* Verify Jacobian determinant = -2 *)
jacobian = D[{F1[x, y, z], F2[x, y, z], F3[x, y, z]}, {{x, y, z}}];
Print["Jacobian determinant: ", Simplify[Det[jacobian]]];
(* Verify the three preimages *)
preimages = {{0, 0, -1/4}, {1, -3/2, 13/2}, {-1, 3/2, 13/2}};
Do[
  pt = preimages[[i]];
  result = {F1 @@ pt, F2 @@ pt, F3 @@ pt};
  Print["F", pt, " = ", result],
  {i, 3}
];


(* Isosurface plot: three level sets in source (x,y,z) space *)
isosurfaces = Show[
  ContourPlot3D[F1[x, y, z] == -1/4, {x, -2, 2}, {y, -3, 3}, {z, -1, 8},
    ContourStyle -> Directive[Blue, Opacity[0.3]],
    Mesh -> None, MaxRecursion -> 3],
  ContourPlot3D[F2[x, y, z] == 0, {x, -2, 2}, {y, -3, 3}, {z, -1, 8},
    ContourStyle -> Directive[Red, Opacity[0.25]],
    Mesh -> None, MaxRecursion -> 3],
  ContourPlot3D[F3[x, y, z] == 0, {x, -2, 2}, {y, -3, 3}, {z, -1, 8},
    ContourStyle -> Directive[Green, Opacity[0.25]],
    Mesh -> None, MaxRecursion -> 3],
  Graphics3D[{
    PointSize[Large], Yellow, EdgeForm[Black],
    Point[{0, 0, -1/4}],
    Point[{1, -3/2, 13/2}],
    Point[{-1, 3/2, 13/2}],
    Black, FontSize -> 12,
    Text["(0, 0, -1/4)", {0, 0, -1/4}, {0, -1.5}],
    Text["(1, -3/2, 13/2)", {1, -3/2, 13/2}, {0, -1.5}],
    Text["(-1, 3/2, 13/2)", {-1, 3/2, 13/2}, {0, -1.5}]
  }],
  AxesLabel -> {"x", "y", "z"},
  PlotLabel -> "Isosurfaces: \!\(\*SubscriptBox[\(F\), \(1\)]\) = -1/4 (blue), \!\(\*SubscriptBox[\(F\), \(2\)]\) = 0 (red), \!\(\*SubscriptBox[\(F\), \(3\)]\) = 0 (green)\nGold points = preimages of (-1/4, 0, 0)",
  ImageSize -> 800,
  BoxRatios -> {1, 1.2, 2}
];


(* Pre-compute the three surfaces (expensive, done once) *)
surfF1 = ContourPlot3D[F1[x, y, z] == -1/4, {x, -2, 2}, {y, -3, 3}, {z, -1, 8},
  ContourStyle -> Directive[Blue, Opacity[0.3]], Mesh -> None, MaxRecursion -> 3];
surfF2 = ContourPlot3D[F2[x, y, z] == 0, {x, -2, 2}, {y, -3, 3}, {z, -1, 8},
  ContourStyle -> Directive[Red, Opacity[0.25]], Mesh -> None, MaxRecursion -> 3];
surfF3 = ContourPlot3D[F3[x, y, z] == 0, {x, -2, 2}, {y, -3, 3}, {z, -1, 8},
  ContourStyle -> Directive[Green, Opacity[0.25]], Mesh -> None, MaxRecursion -> 3];


preimagePoints = Graphics3D[{
  PointSize[Large], Yellow, EdgeForm[Black],
  Point[{0, 0, -1/4}],
  Point[{1, -3/2, 13/2}],
  Point[{-1, 3/2, 13/2}],
  Black, FontSize -> 12,
  Text["(0, 0, -1/4)", {0, 0, -1/4}, {0, -1.5}],
  Text["(1, -3/2, 13/2)", {1, -3/2, 13/2}, {0, -1.5}],
  Text["(-1, 3/2, 13/2)", {-1, 3/2, 13/2}, {0, -1.5}]
}];


(* Lightweight opacity swap on pre-computed graphics *)
setOpacity[surf_, op_] := surf /. Opacity[_] -> Opacity[op];

(* Interactive version: toggles + opacity sliders, no recomputation *)
manipulate = Manipulate[
  Column[{
    Style["Jacobian Conjecture Counterexample (Alpoge, 2026)", Bold, 16],
    Style["Isosurfaces of \!\(\*SubscriptBox[\(F\), \(1\)]\) = \[Minus]1/4, \!\(\*SubscriptBox[\(F\), \(2\)]\) = 0, \!\(\*SubscriptBox[\(F\), \(3\)]\) = 0 in source (x, y, z) space\nGold points = three preimages of (\[Minus]1/4, 0, 0)", Gray, 11],
    Spacer[5],
  Show[
    Sequence @@ Select[{
      If[showF1, setOpacity[surfF1, opF1], Nothing],
      If[showF2, setOpacity[surfF2, opF2], Nothing],
      If[showF3, setOpacity[surfF3, opF3], Nothing],
      preimagePoints
    }, True &],
    AxesLabel -> {"x", "y", "z"},
    BoxRatios -> {1, 1.2, 2},
    ImageSize -> 800
  ],
    Spacer[5],
    Style["Visualization by Claude Opus 4.6", Italic, Gray, 9]
  }],
  Delimiter, Style["Surfaces", Bold],
  {{showF1, True, "\!\(\*SubscriptBox[\(F\), \(1\)]\) = -1/4 (blue)"}, {True, False}},
  {{showF2, True, "\!\(\*SubscriptBox[\(F\), \(2\)]\) = 0 (red)"}, {True, False}},
  {{showF3, True, "\!\(\*SubscriptBox[\(F\), \(3\)]\) = 0 (green)"}, {True, False}},
  Delimiter, Style["Appearance", Bold],
  {{opF1, 0.3, "Blue opacity"}, 0.05, 0.8},
  {{opF2, 0.25, "Red opacity"}, 0.05, 0.8},
  {{opF3, 0.25, "Green opacity"}, 0.05, 0.8},
  ControlPlacement -> Left,
  SaveDefinitions -> True
]


(* Export as CDF: *)
CDFDeploy["JacobianConjecture.cdf", manipulate];


(* Export static image: *)
(*Export["isosurfaces.png", isosurfaces, ImageResolution -> 300];*)
