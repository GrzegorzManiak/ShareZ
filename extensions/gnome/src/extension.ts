import GLib from "gi://GLib";
import Logger from "./logger/log";
import { Extension } from '@girs/gnome-shell/extensions/extension';

export default class extends Extension {

    public enable() {
        Logger.info('Enabling extension');
    }

    public disable() {
        Logger.info('Disabling extension');
    }
}