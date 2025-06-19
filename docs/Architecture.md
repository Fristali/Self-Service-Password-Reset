# Architecture

```
+-------------------+      +-------------------+      +-------------------+
|  User Browser     |<---->|   Flask App       |<---->|  PowerShell Script|
+-------------------+      +-------------------+      +-------------------+
        |                        |                             |
        |                        |                             |
        v                        v                             v
+-------------------+      +-------------------+      +-------------------+
|  Bootstrap UI     |      |  SQLite Lockout   |      |  AD (Simulated)   |
+-------------------+      +-------------------+      +-------------------+
        |                        |                             |
        v                        v                             v
+-------------------+      +-------------------+      +-------------------+
|  users.csv        |      |  ELK Sample Logs  |      |  Kibana Dashboard |
+-------------------+      +-------------------+      +-------------------+
```

## Draw.io XML

```xml
<mxfile host="app.diagrams.net">
  <diagram id="1" name="Password Reset Portal">
    <mxGraphModel dx="1000" dy="600" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169">
      <root>
        <mxCell id="0"/>
        <mxCell id="1" parent="0"/>
        <mxCell id="2" value="User Browser" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="40" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="3" value="Flask App" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="40" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="4" value="PowerShell Script" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="40" width="140" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="5" value="Bootstrap UI" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="140" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="6" value="SQLite Lockout" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="140" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="7" value="AD (Simulated)" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="140" width="140" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="8" value="users.csv" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="40" y="240" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="9" value="ELK Sample Logs" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="200" y="240" width="120" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="10" value="Kibana Dashboard" style="rounded=1;whiteSpace=wrap;html=1;" vertex="1" parent="1">
          <mxGeometry x="360" y="240" width="140" height="60" as="geometry"/>
        </mxCell>
        <mxCell id="11" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="2" target="3">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="12" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=1;exitY=0.5;exitDx=0;exitDy=0;entryX=0;entryY=0.5;entryDx=0;entryDy=0;" edge="1" parent="1" source="3" target="4">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="13" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="2" target="5">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="14" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="3" target="6">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="15" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="4" target="7">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="16" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="5" target="8">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="17" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="6" target="9">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
        <mxCell id="18" style="edgeStyle=orthogonalEdgeStyle;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=1;exitDx=0;exitDy=0;entryX=0.5;entryY=0;entryDx=0;entryDy=0;" edge="1" parent="1" source="7" target="10">
          <mxGeometry relative="1" as="geometry"/>
        </mxCell>
      </root>
    </mxGraphModel>
  </diagram>
</mxfile>
```
