export default class Window {
    private _title: string;

    private _x: number;
    private _y: number;

    private _width: number;
    private _height: number;

    private _z_index: number;



    /**
     * @name Window
     * Standard window object that will be sent over dbus
     *
     * @param {string} title - The title of the window
     * @param {number} x - The x position of the window
     * @param {number} y - The y position of the window
     * @param {number} width - The width of the window
     * @param {number} height - The height of the window
     * @param {number} z_index - The z-index of the window (The order in which it is displayed)
     */
    public constructor(
        title: string,
        x: number,
        y: number,
        width: number,
        height: number,
        z_index: number
    ) {
        this._title = title;
        this._x = x;
        this._y = y;
        this._width = width;
        this._height = height;
        this._z_index = z_index;
    }
}