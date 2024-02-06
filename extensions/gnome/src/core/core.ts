import Window from './window';
import { Extension } from 'resource:///org/gnome/shell/extensions/extension.js';
import { LayoutManager } from 'resource:///org/gnome/shell/ui/layout.js';

import GLib from 'gi://GLib';
import Meta from 'gi://Meta';

import Shell from 'gi://Shell';
import Logger from '../logger/log';
import Display from './display';
const global = Shell.Global.get();



/**
 * @name get_open_windows
 * Returns a list of open windows
 *
 * @returns {Array<Window>} - A list of open windows
 */
export const get_open_windows = (): Array<Window> => {
    const windows: Array<Window> = [];

    // -- Get all open windows
    const open_windows = global.get_window_actors();
    open_windows.forEach((open_window) => {

        // -- Get the actual window
        const meta_window = open_window.get_meta_window();
        Logger.info('Window: ' + meta_window.get_title());

        // -- Create a new window object
        windows.push(new Window(
            meta_window.get_title(),
            meta_window.get_frame_rect().x,
            meta_window.get_frame_rect().y,
            meta_window.get_frame_rect().width,
            meta_window.get_frame_rect().height,
            meta_window.get_layer()
        ));
    });

    Logger.info('Found ' + windows.length + ' open windows');
    return windows;
};



/**
 * @name get_focused_window
 * Returns the focused window
 *
 * @returns {Window | null} - The focused window or null if there is no focused window
 */
export const get_focused_window = (): Window | null => {
    const meta_window = global.display.get_focus_window();
    if (!meta_window) return null;
    Logger.info('Focused window: ' + meta_window.get_title());
    return new Window(
        meta_window.get_title(),
        meta_window.get_frame_rect().x,
        meta_window.get_frame_rect().y,
        meta_window.get_frame_rect().width,
        meta_window.get_frame_rect().height,
        meta_window.get_layer()
    );
}



/**
 * @name get_all_displays
 * Returns a list of displays (monitors)
 *
 * @returns {Array<Display>} - A list of displays
 */
export const get_all_displays = (): Array<Display> => {
    const displays: Array<Display> = [];

    // -- Get all monitors
    const monitors = new LayoutManager().monitors;
    monitors.forEach((monitor) => displays.push(new Display(
        monitor.x, monitor.y,
        monitor.width, monitor.height,
        monitor.index
    )));

    Logger.info('Found ' + displays.length + ' displays');
    return displays;
}