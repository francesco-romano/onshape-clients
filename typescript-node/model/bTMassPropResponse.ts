/**
 * Onshape REST API
 * The Onshape REST API consumed by all clients.
 *
 * OpenAPI spec version: 1.93
 * Contact: api-support@onshape.zendesk.com
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */

import { BTConnection } from './bTConnection';
import { BTMassProperties } from './bTMassProperties';

export class BTMassPropResponse {
    'microversionId'?: string;
    'bodies'?: { [key: string]: BTMassProperties; };
    'typeId'?: number;
    'exportTypeName'?: string;
    'connectionSource'?: BTConnection;
    'unknownClass'?: boolean;

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "microversionId",
            "baseName": "microversionId",
            "type": "string"
        },
        {
            "name": "bodies",
            "baseName": "bodies",
            "type": "{ [key: string]: BTMassProperties; }"
        },
        {
            "name": "typeId",
            "baseName": "typeId",
            "type": "number"
        },
        {
            "name": "exportTypeName",
            "baseName": "exportTypeName",
            "type": "string"
        },
        {
            "name": "connectionSource",
            "baseName": "connectionSource",
            "type": "BTConnection"
        },
        {
            "name": "unknownClass",
            "baseName": "unknownClass",
            "type": "boolean"
        }    ];

    static getAttributeTypeMap() {
        return BTMassPropResponse.attributeTypeMap;
    }
}

