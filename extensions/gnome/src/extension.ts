import { Extension } from "resource:///org/gnome/shell/extensions/extension.js";
import Logger from "./logger/log";
import DBus from "./dbus/dbus";

export default class ShareZ extends Extension {
    private static _dbus: DBus;

    public enable() {
        Logger.info('SHAREZ Enabling extension');

        if (!ShareZ._dbus) ShareZ._dbus = DBus.getInstance();
        ShareZ._dbus.acquire_bus();
    }
    public disable() {
        Logger.info('SHAREZ Disabling extension');
        if (ShareZ._dbus) ShareZ._dbus.release_bus();
    }
}