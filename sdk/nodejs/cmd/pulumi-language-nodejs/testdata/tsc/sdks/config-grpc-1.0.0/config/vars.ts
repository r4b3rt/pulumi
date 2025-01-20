// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

declare var exports: any;
const __config = new pulumi.Config("config-grpc");

export declare const bool1: boolean | undefined;
Object.defineProperty(exports, "bool1", {
    get() {
        return __config.getObject<boolean>("bool1");
    },
    enumerable: true,
});

export declare const bool2: boolean | undefined;
Object.defineProperty(exports, "bool2", {
    get() {
        return __config.getObject<boolean>("bool2");
    },
    enumerable: true,
});

export declare const bool3: boolean | undefined;
Object.defineProperty(exports, "bool3", {
    get() {
        return __config.getObject<boolean>("bool3");
    },
    enumerable: true,
});

export declare const int1: number | undefined;
Object.defineProperty(exports, "int1", {
    get() {
        return __config.getObject<number>("int1");
    },
    enumerable: true,
});

export declare const int2: number | undefined;
Object.defineProperty(exports, "int2", {
    get() {
        return __config.getObject<number>("int2");
    },
    enumerable: true,
});

export declare const int3: number | undefined;
Object.defineProperty(exports, "int3", {
    get() {
        return __config.getObject<number>("int3");
    },
    enumerable: true,
});

export declare const listBool1: boolean[] | undefined;
Object.defineProperty(exports, "listBool1", {
    get() {
        return __config.getObject<boolean[]>("listBool1");
    },
    enumerable: true,
});

export declare const listBool2: boolean[] | undefined;
Object.defineProperty(exports, "listBool2", {
    get() {
        return __config.getObject<boolean[]>("listBool2");
    },
    enumerable: true,
});

export declare const listBool3: boolean[] | undefined;
Object.defineProperty(exports, "listBool3", {
    get() {
        return __config.getObject<boolean[]>("listBool3");
    },
    enumerable: true,
});

export declare const listInt1: number[] | undefined;
Object.defineProperty(exports, "listInt1", {
    get() {
        return __config.getObject<number[]>("listInt1");
    },
    enumerable: true,
});

export declare const listInt2: number[] | undefined;
Object.defineProperty(exports, "listInt2", {
    get() {
        return __config.getObject<number[]>("listInt2");
    },
    enumerable: true,
});

export declare const listInt3: number[] | undefined;
Object.defineProperty(exports, "listInt3", {
    get() {
        return __config.getObject<number[]>("listInt3");
    },
    enumerable: true,
});

export declare const listNum1: number[] | undefined;
Object.defineProperty(exports, "listNum1", {
    get() {
        return __config.getObject<number[]>("listNum1");
    },
    enumerable: true,
});

export declare const listNum2: number[] | undefined;
Object.defineProperty(exports, "listNum2", {
    get() {
        return __config.getObject<number[]>("listNum2");
    },
    enumerable: true,
});

export declare const listNum3: number[] | undefined;
Object.defineProperty(exports, "listNum3", {
    get() {
        return __config.getObject<number[]>("listNum3");
    },
    enumerable: true,
});

export declare const listSecretBool1: boolean[] | undefined;
Object.defineProperty(exports, "listSecretBool1", {
    get() {
        return __config.getObject<boolean[]>("listSecretBool1");
    },
    enumerable: true,
});

export declare const listSecretBool2: boolean[] | undefined;
Object.defineProperty(exports, "listSecretBool2", {
    get() {
        return __config.getObject<boolean[]>("listSecretBool2");
    },
    enumerable: true,
});

export declare const listSecretBool3: boolean[] | undefined;
Object.defineProperty(exports, "listSecretBool3", {
    get() {
        return __config.getObject<boolean[]>("listSecretBool3");
    },
    enumerable: true,
});

export declare const listSecretInt1: number[] | undefined;
Object.defineProperty(exports, "listSecretInt1", {
    get() {
        return __config.getObject<number[]>("listSecretInt1");
    },
    enumerable: true,
});

export declare const listSecretInt2: number[] | undefined;
Object.defineProperty(exports, "listSecretInt2", {
    get() {
        return __config.getObject<number[]>("listSecretInt2");
    },
    enumerable: true,
});

export declare const listSecretInt3: number[] | undefined;
Object.defineProperty(exports, "listSecretInt3", {
    get() {
        return __config.getObject<number[]>("listSecretInt3");
    },
    enumerable: true,
});

export declare const listSecretNum1: number[] | undefined;
Object.defineProperty(exports, "listSecretNum1", {
    get() {
        return __config.getObject<number[]>("listSecretNum1");
    },
    enumerable: true,
});

export declare const listSecretNum2: number[] | undefined;
Object.defineProperty(exports, "listSecretNum2", {
    get() {
        return __config.getObject<number[]>("listSecretNum2");
    },
    enumerable: true,
});

export declare const listSecretNum3: number[] | undefined;
Object.defineProperty(exports, "listSecretNum3", {
    get() {
        return __config.getObject<number[]>("listSecretNum3");
    },
    enumerable: true,
});

export declare const listSecretString1: string[] | undefined;
Object.defineProperty(exports, "listSecretString1", {
    get() {
        return __config.getObject<string[]>("listSecretString1");
    },
    enumerable: true,
});

export declare const listSecretString2: string[] | undefined;
Object.defineProperty(exports, "listSecretString2", {
    get() {
        return __config.getObject<string[]>("listSecretString2");
    },
    enumerable: true,
});

export declare const listSecretString3: string[] | undefined;
Object.defineProperty(exports, "listSecretString3", {
    get() {
        return __config.getObject<string[]>("listSecretString3");
    },
    enumerable: true,
});

export declare const listString1: string[] | undefined;
Object.defineProperty(exports, "listString1", {
    get() {
        return __config.getObject<string[]>("listString1");
    },
    enumerable: true,
});

export declare const listString2: string[] | undefined;
Object.defineProperty(exports, "listString2", {
    get() {
        return __config.getObject<string[]>("listString2");
    },
    enumerable: true,
});

export declare const listString3: string[] | undefined;
Object.defineProperty(exports, "listString3", {
    get() {
        return __config.getObject<string[]>("listString3");
    },
    enumerable: true,
});

export declare const mapBool1: {[key: string]: boolean} | undefined;
Object.defineProperty(exports, "mapBool1", {
    get() {
        return __config.getObject<{[key: string]: boolean}>("mapBool1");
    },
    enumerable: true,
});

export declare const mapBool2: {[key: string]: boolean} | undefined;
Object.defineProperty(exports, "mapBool2", {
    get() {
        return __config.getObject<{[key: string]: boolean}>("mapBool2");
    },
    enumerable: true,
});

export declare const mapBool3: {[key: string]: boolean} | undefined;
Object.defineProperty(exports, "mapBool3", {
    get() {
        return __config.getObject<{[key: string]: boolean}>("mapBool3");
    },
    enumerable: true,
});

export declare const mapInt1: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapInt1", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapInt1");
    },
    enumerable: true,
});

export declare const mapInt2: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapInt2", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapInt2");
    },
    enumerable: true,
});

export declare const mapInt3: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapInt3", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapInt3");
    },
    enumerable: true,
});

export declare const mapNum1: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapNum1", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapNum1");
    },
    enumerable: true,
});

export declare const mapNum2: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapNum2", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapNum2");
    },
    enumerable: true,
});

export declare const mapNum3: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapNum3", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapNum3");
    },
    enumerable: true,
});

export declare const mapSecretBool1: {[key: string]: boolean} | undefined;
Object.defineProperty(exports, "mapSecretBool1", {
    get() {
        return __config.getObject<{[key: string]: boolean}>("mapSecretBool1");
    },
    enumerable: true,
});

export declare const mapSecretBool2: {[key: string]: boolean} | undefined;
Object.defineProperty(exports, "mapSecretBool2", {
    get() {
        return __config.getObject<{[key: string]: boolean}>("mapSecretBool2");
    },
    enumerable: true,
});

export declare const mapSecretBool3: {[key: string]: boolean} | undefined;
Object.defineProperty(exports, "mapSecretBool3", {
    get() {
        return __config.getObject<{[key: string]: boolean}>("mapSecretBool3");
    },
    enumerable: true,
});

export declare const mapSecretInt1: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapSecretInt1", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapSecretInt1");
    },
    enumerable: true,
});

export declare const mapSecretInt2: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapSecretInt2", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapSecretInt2");
    },
    enumerable: true,
});

export declare const mapSecretInt3: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapSecretInt3", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapSecretInt3");
    },
    enumerable: true,
});

export declare const mapSecretNum1: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapSecretNum1", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapSecretNum1");
    },
    enumerable: true,
});

export declare const mapSecretNum2: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapSecretNum2", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapSecretNum2");
    },
    enumerable: true,
});

export declare const mapSecretNum3: {[key: string]: number} | undefined;
Object.defineProperty(exports, "mapSecretNum3", {
    get() {
        return __config.getObject<{[key: string]: number}>("mapSecretNum3");
    },
    enumerable: true,
});

export declare const mapSecretString1: {[key: string]: string} | undefined;
Object.defineProperty(exports, "mapSecretString1", {
    get() {
        return __config.getObject<{[key: string]: string}>("mapSecretString1");
    },
    enumerable: true,
});

export declare const mapSecretString2: {[key: string]: string} | undefined;
Object.defineProperty(exports, "mapSecretString2", {
    get() {
        return __config.getObject<{[key: string]: string}>("mapSecretString2");
    },
    enumerable: true,
});

export declare const mapSecretString3: {[key: string]: string} | undefined;
Object.defineProperty(exports, "mapSecretString3", {
    get() {
        return __config.getObject<{[key: string]: string}>("mapSecretString3");
    },
    enumerable: true,
});

export declare const mapString1: {[key: string]: string} | undefined;
Object.defineProperty(exports, "mapString1", {
    get() {
        return __config.getObject<{[key: string]: string}>("mapString1");
    },
    enumerable: true,
});

export declare const mapString2: {[key: string]: string} | undefined;
Object.defineProperty(exports, "mapString2", {
    get() {
        return __config.getObject<{[key: string]: string}>("mapString2");
    },
    enumerable: true,
});

export declare const mapString3: {[key: string]: string} | undefined;
Object.defineProperty(exports, "mapString3", {
    get() {
        return __config.getObject<{[key: string]: string}>("mapString3");
    },
    enumerable: true,
});

export declare const num1: number | undefined;
Object.defineProperty(exports, "num1", {
    get() {
        return __config.getObject<number>("num1");
    },
    enumerable: true,
});

export declare const num2: number | undefined;
Object.defineProperty(exports, "num2", {
    get() {
        return __config.getObject<number>("num2");
    },
    enumerable: true,
});

export declare const num3: number | undefined;
Object.defineProperty(exports, "num3", {
    get() {
        return __config.getObject<number>("num3");
    },
    enumerable: true,
});

export declare const objBool1: outputs.Tbool1 | undefined;
Object.defineProperty(exports, "objBool1", {
    get() {
        return __config.getObject<outputs.Tbool1>("objBool1");
    },
    enumerable: true,
});

export declare const objBool2: outputs.Tbool2 | undefined;
Object.defineProperty(exports, "objBool2", {
    get() {
        return __config.getObject<outputs.Tbool2>("objBool2");
    },
    enumerable: true,
});

export declare const objBool3: outputs.Tbool3 | undefined;
Object.defineProperty(exports, "objBool3", {
    get() {
        return __config.getObject<outputs.Tbool3>("objBool3");
    },
    enumerable: true,
});

export declare const objInt1: outputs.Tint1 | undefined;
Object.defineProperty(exports, "objInt1", {
    get() {
        return __config.getObject<outputs.Tint1>("objInt1");
    },
    enumerable: true,
});

export declare const objInt2: outputs.Tint2 | undefined;
Object.defineProperty(exports, "objInt2", {
    get() {
        return __config.getObject<outputs.Tint2>("objInt2");
    },
    enumerable: true,
});

export declare const objInt3: outputs.Tint3 | undefined;
Object.defineProperty(exports, "objInt3", {
    get() {
        return __config.getObject<outputs.Tint3>("objInt3");
    },
    enumerable: true,
});

export declare const objNum1: outputs.Tnum1 | undefined;
Object.defineProperty(exports, "objNum1", {
    get() {
        return __config.getObject<outputs.Tnum1>("objNum1");
    },
    enumerable: true,
});

export declare const objNum2: outputs.Tnum2 | undefined;
Object.defineProperty(exports, "objNum2", {
    get() {
        return __config.getObject<outputs.Tnum2>("objNum2");
    },
    enumerable: true,
});

export declare const objNum3: outputs.Tnum3 | undefined;
Object.defineProperty(exports, "objNum3", {
    get() {
        return __config.getObject<outputs.Tnum3>("objNum3");
    },
    enumerable: true,
});

export declare const objSecretBool1: outputs.TsecretBool1 | undefined;
Object.defineProperty(exports, "objSecretBool1", {
    get() {
        return __config.getObject<outputs.TsecretBool1>("objSecretBool1");
    },
    enumerable: true,
});

export declare const objSecretBool2: outputs.TsecretBool2 | undefined;
Object.defineProperty(exports, "objSecretBool2", {
    get() {
        return __config.getObject<outputs.TsecretBool2>("objSecretBool2");
    },
    enumerable: true,
});

export declare const objSecretBool3: outputs.TsecretBool3 | undefined;
Object.defineProperty(exports, "objSecretBool3", {
    get() {
        return __config.getObject<outputs.TsecretBool3>("objSecretBool3");
    },
    enumerable: true,
});

export declare const objSecretInt1: outputs.TsecretInt1 | undefined;
Object.defineProperty(exports, "objSecretInt1", {
    get() {
        return __config.getObject<outputs.TsecretInt1>("objSecretInt1");
    },
    enumerable: true,
});

export declare const objSecretInt2: outputs.TsecretInt2 | undefined;
Object.defineProperty(exports, "objSecretInt2", {
    get() {
        return __config.getObject<outputs.TsecretInt2>("objSecretInt2");
    },
    enumerable: true,
});

export declare const objSecretInt3: outputs.TsecretInt3 | undefined;
Object.defineProperty(exports, "objSecretInt3", {
    get() {
        return __config.getObject<outputs.TsecretInt3>("objSecretInt3");
    },
    enumerable: true,
});

export declare const objSecretNum1: outputs.TsecretNum1 | undefined;
Object.defineProperty(exports, "objSecretNum1", {
    get() {
        return __config.getObject<outputs.TsecretNum1>("objSecretNum1");
    },
    enumerable: true,
});

export declare const objSecretNum2: outputs.TsecretNum2 | undefined;
Object.defineProperty(exports, "objSecretNum2", {
    get() {
        return __config.getObject<outputs.TsecretNum2>("objSecretNum2");
    },
    enumerable: true,
});

export declare const objSecretNum3: outputs.TsecretNum3 | undefined;
Object.defineProperty(exports, "objSecretNum3", {
    get() {
        return __config.getObject<outputs.TsecretNum3>("objSecretNum3");
    },
    enumerable: true,
});

export declare const objSecretString1: outputs.TsecretString1 | undefined;
Object.defineProperty(exports, "objSecretString1", {
    get() {
        return __config.getObject<outputs.TsecretString1>("objSecretString1");
    },
    enumerable: true,
});

export declare const objSecretString2: outputs.TsecretString2 | undefined;
Object.defineProperty(exports, "objSecretString2", {
    get() {
        return __config.getObject<outputs.TsecretString2>("objSecretString2");
    },
    enumerable: true,
});

export declare const objSecretString3: outputs.TsecretString3 | undefined;
Object.defineProperty(exports, "objSecretString3", {
    get() {
        return __config.getObject<outputs.TsecretString3>("objSecretString3");
    },
    enumerable: true,
});

export declare const objString1: outputs.Tstring1 | undefined;
Object.defineProperty(exports, "objString1", {
    get() {
        return __config.getObject<outputs.Tstring1>("objString1");
    },
    enumerable: true,
});

export declare const objString2: outputs.Tstring2 | undefined;
Object.defineProperty(exports, "objString2", {
    get() {
        return __config.getObject<outputs.Tstring2>("objString2");
    },
    enumerable: true,
});

export declare const objString3: outputs.Tstring3 | undefined;
Object.defineProperty(exports, "objString3", {
    get() {
        return __config.getObject<outputs.Tstring3>("objString3");
    },
    enumerable: true,
});

export declare const secretBool1: boolean | undefined;
Object.defineProperty(exports, "secretBool1", {
    get() {
        return __config.getObject<boolean>("secretBool1");
    },
    enumerable: true,
});

export declare const secretBool2: boolean | undefined;
Object.defineProperty(exports, "secretBool2", {
    get() {
        return __config.getObject<boolean>("secretBool2");
    },
    enumerable: true,
});

export declare const secretBool3: boolean | undefined;
Object.defineProperty(exports, "secretBool3", {
    get() {
        return __config.getObject<boolean>("secretBool3");
    },
    enumerable: true,
});

export declare const secretInt1: number | undefined;
Object.defineProperty(exports, "secretInt1", {
    get() {
        return __config.getObject<number>("secretInt1");
    },
    enumerable: true,
});

export declare const secretInt2: number | undefined;
Object.defineProperty(exports, "secretInt2", {
    get() {
        return __config.getObject<number>("secretInt2");
    },
    enumerable: true,
});

export declare const secretInt3: number | undefined;
Object.defineProperty(exports, "secretInt3", {
    get() {
        return __config.getObject<number>("secretInt3");
    },
    enumerable: true,
});

export declare const secretNum1: number | undefined;
Object.defineProperty(exports, "secretNum1", {
    get() {
        return __config.getObject<number>("secretNum1");
    },
    enumerable: true,
});

export declare const secretNum2: number | undefined;
Object.defineProperty(exports, "secretNum2", {
    get() {
        return __config.getObject<number>("secretNum2");
    },
    enumerable: true,
});

export declare const secretNum3: number | undefined;
Object.defineProperty(exports, "secretNum3", {
    get() {
        return __config.getObject<number>("secretNum3");
    },
    enumerable: true,
});

export declare const secretString1: string | undefined;
Object.defineProperty(exports, "secretString1", {
    get() {
        return __config.get("secretString1");
    },
    enumerable: true,
});

export declare const secretString2: string | undefined;
Object.defineProperty(exports, "secretString2", {
    get() {
        return __config.get("secretString2");
    },
    enumerable: true,
});

export declare const secretString3: string | undefined;
Object.defineProperty(exports, "secretString3", {
    get() {
        return __config.get("secretString3");
    },
    enumerable: true,
});

export declare const string1: string | undefined;
Object.defineProperty(exports, "string1", {
    get() {
        return __config.get("string1");
    },
    enumerable: true,
});

export declare const string2: string | undefined;
Object.defineProperty(exports, "string2", {
    get() {
        return __config.get("string2");
    },
    enumerable: true,
});

export declare const string3: string | undefined;
Object.defineProperty(exports, "string3", {
    get() {
        return __config.get("string3");
    },
    enumerable: true,
});

