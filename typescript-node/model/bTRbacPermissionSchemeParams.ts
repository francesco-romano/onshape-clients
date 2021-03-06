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

import { BTPermissionSet } from './bTPermissionSet';

export class BTRbacPermissionSchemeParams {
    'name'?: string;
    'description'?: string;
    'permissionMap'?: { [key: string]: BTPermissionSet; };

    static discriminator: string | undefined = undefined;

    static attributeTypeMap: Array<{name: string, baseName: string, type: string}> = [
        {
            "name": "name",
            "baseName": "name",
            "type": "string"
        },
        {
            "name": "description",
            "baseName": "description",
            "type": "string"
        },
        {
            "name": "permissionMap",
            "baseName": "permissionMap",
            "type": "{ [key: string]: BTPermissionSet; }"
        }    ];

    static getAttributeTypeMap() {
        return BTRbacPermissionSchemeParams.attributeTypeMap;
    }
}

