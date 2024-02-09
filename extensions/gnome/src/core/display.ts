export default class Display {

    private _x: number;
    private _y: number;

    private _width: number;
    private _height: number;

    private _index: number;


    /**
     * @name Display
     * Standard display object that will be sent over dbus
     *
     * @param {number} x - The x position of the display
     * @param {number} y - The y position of the display
     * @param {number} width - The width of the display
     * @param {number} height - The height of the display
     * @param {number} index - The z-index of the display (The order in which it is displayed)
     */
    public constructor(
        x: number,
        y: number,
        width: number,
        height: number,
        index: number
    ) {
        this._x = x;
        this._y = y;
        this._width = width;
        this._height = height;
        this._index = index;
    }



    get index(): number {
        return this._index;
    }
}