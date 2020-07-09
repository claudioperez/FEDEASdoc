## Model Type

`object` ([Model](model.md))

# Model Properties

| Property              | Type      | Required | Nullable       | Defined by                                                                                                                                                  |
| :-------------------- | --------- | -------- | -------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [nn](#nn)             | `integer` | Required | cannot be null | [Model](model-properties-nn.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nn")             |
| [ndm](#ndm)           | `integer` | Required | cannot be null | [Model](model-properties-ndm.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ndm")           |
| [XYZ](#XYZ)           | `array`   | Required | cannot be null | [Model](model-properties-xyz.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/XYZ")           |
| [ne](#ne)             | `integer` | Required | cannot be null | [Model](model-properties-ne.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ne")             |
| [CON](#CON)           | Merged    | Required | cannot be null | [Model](model-properties-con.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/CON")           |
| [nen](#nen)           | Merged    | Required | cannot be null | [Model](model-properties-nen.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nen")           |
| [ndf](#ndf)           | Merged    | Required | cannot be null | [Model](model-properties-ndf.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ndf")           |
| [ElemName](#ElemName) | `array`   | Required | cannot be null | [Model](model-properties-elemname.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ElemName") |
| [DOF](#DOF)           | `array`   | Required | cannot be null | [Model](model-properties-dof.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/DOF")           |
| [nt](#nt)             | `integer` | Required | cannot be null | [Model](model-properties-nt.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nt")             |
| [BOUN](#BOUN)         | `array`   | Required | cannot be null | [Model](model-properties-boun.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/BOUN")         |
| [nf](#nf)             | `integer` | Required | cannot be null | [Model](model-properties-nf.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nf")             |
| [ntrm](#ntrm)         | `integer` | Required | cannot be null | [Model](model-properties-ntrm.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ntrm")         |
| [nq](#nq)             | `integer` | Optional | cannot be null | [Model](model-properties-nq.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nq")             |

## nn

number of nodes in structural model


`nn`

-   is required
-   Type: `integer` ([nn](model-properties-nn.md))
-   cannot be null
-   defined in: [Model](model-properties-nn.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nn")
-   description: number of nodes in structural model

### nn Type

`integer` ([nn](model-properties-nn.md))

## ndm

dimension of structural model


`ndm`

-   is required
-   Type: `integer` ([ndm](model-properties-ndm.md))
-   cannot be null
-   defined in: [Model](model-properties-ndm.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ndm")
-   description: dimension of structural model

### ndm Type

`integer` ([ndm](model-properties-ndm.md))

## XYZ

array holding spacial coordinates of model nodes.


`XYZ`

-   is required
-   Type: an array of merged types ([Details](model-properties-xyz-items.md))
-   cannot be null
-   defined in: [Model](model-properties-xyz.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/XYZ")
-   description: array holding spacial coordinates of model nodes.

### XYZ Type

an array of merged types ([Details](model-properties-xyz-items.md))

## ne

number of elements in model.


`ne`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [Model](model-properties-ne.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ne")
-   description: number of elements in model.

### ne Type

`integer`

## CON




`CON`

-   is required
-   Type: merged type ([CON](model-properties-con.md))
-   cannot be null
-   defined in: [Model](model-properties-con.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/CON")

### CON Type

merged type ([CON](model-properties-con.md))

any of

-   [Untitled integer in Model](model-properties-con-anyof-0.md "check type definition")
-   [Untitled array in Model](model-properties-con-anyof-1.md "check type definition")

## nen




`nen`

-   is required
-   Type: merged type ([Details](model-properties-nen.md))
-   cannot be null
-   defined in: [Model](model-properties-nen.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nen")

### nen Type

merged type ([Details](model-properties-nen.md))

any of

-   [Untitled integer in Model](model-properties-nen-anyof-0.md "check type definition")
-   [Untitled array in Model](model-properties-nen-anyof-1.md "check type definition")

## ndf




`ndf`

-   is required
-   Type: merged type ([Details](model-properties-ndf.md))
-   cannot be null
-   defined in: [Model](model-properties-ndf.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ndf")

### ndf Type

merged type ([Details](model-properties-ndf.md))

any of

-   [Untitled integer in Model](model-properties-ndf-anyof-0.md "check type definition")
-   [Untitled array in Model](model-properties-ndf-anyof-1.md "check type definition")

## ElemName




`ElemName`

-   is required
-   Type: `string[]`
-   cannot be null
-   defined in: [Model](model-properties-elemname.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ElemName")

### ElemName Type

`string[]`

## DOF

array with degree of freedom numbering


`DOF`

-   is required
-   Type: an array of merged types ([Details](model-properties-dof-items.md))
-   cannot be null
-   defined in: [Model](model-properties-dof.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/DOF")
-   description: array with degree of freedom numbering

### DOF Type

an array of merged types ([Details](model-properties-dof-items.md))

## nt




`nt`

-   is required
-   Type: `integer` ([nt](model-properties-nt.md))
-   cannot be null
-   defined in: [Model](model-properties-nt.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nt")

### nt Type

`integer` ([nt](model-properties-nt.md))

## BOUN




`BOUN`

-   is required
-   Type: an array of merged types ([Details](model-properties-boun-items.md))
-   cannot be null
-   defined in: [Model](model-properties-boun.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/BOUN")

### BOUN Type

an array of merged types ([Details](model-properties-boun-items.md))

## nf

number of free degrees of freedom


`nf`

-   is required
-   Type: `integer` ([nf](model-properties-nf.md))
-   cannot be null
-   defined in: [Model](model-properties-nf.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nf")
-   description: number of free degrees of freedom

### nf Type

`integer` ([nf](model-properties-nf.md))

## ntrm




`ntrm`

-   is required
-   Type: `integer`
-   cannot be null
-   defined in: [Model](model-properties-ntrm.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/ntrm")

### ntrm Type

`integer`

## nq




`nq`

-   is optional
-   Type: `integer`
-   cannot be null
-   defined in: [Model](model-properties-nq.md "https&#x3A;//raw.githubusercontent.com/claudioperez/FedeasAPI/v0.0.0/schemas/model.schema.json#/properties/nq")

### nq Type

`integer`
