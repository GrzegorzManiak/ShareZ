import GLib from "gi://GLib";
import { Extension } from "resource:///org/gnome/shell/extensions/extension.js";
import Logger from "./logger/log.js";

export default class extends Extension {

    public enable() {
        Logger.info('Enabling extension');
    }

    public disable() {
        Logger.info('Disabling extension');
        
    }
}