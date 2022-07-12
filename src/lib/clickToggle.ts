type Options = {
    item?: string
    outside?: boolean
    save?: boolean
    key?: string
}

const CLASS_NAME = 'visible'

/**
 * Toggle visible and hidden an element.
 *
 * The element to toggle should be exactly after the one that uses the action.
 *
 * @param element The element that uses the action, should not be passed.
 * @param options.item The item that will be toggled.
 * Use `next` to use the one immediately after the `element`.
 *
 * @param options.save Specify if the element should be save to localStorage or not.
 * @param options.key The key to be saved to localStorage, only work if save is true.
 *
 * @returns Nothing, just remove Event Listenner.
 */

export function clickInside(element: Element, options?: Options) {
    // This occurs when clickOutside is used in an element other than clickInside.

    function onClick() {
        let item: Element = element

        if ((options) && (options.item)) {
            if (options.item !== 'next') {
                item = document.querySelector(options.item) || item
            }
            else {
                item = element.nextElementSibling || item
            }
        }

        item.dispatchEvent(new CustomEvent('clickInside'))
        item.classList.toggle(CLASS_NAME)

        if (options) {
            if ((options.save) && (options.key)) {
                const hasClass = item.classList.contains(CLASS_NAME)
                localStorage.setItem(options.key, hasClass.toString())
            }

            if (options.outside) {
                clickOutside(item, element)
            }
        }
    }

    element.addEventListener('click', onClick, true)

    return {
        destroy() {
            element.removeEventListener('click', onClick, true)
        }
    }
}
/**
 * Hides a visible element when click outside it.
 *
 * Use it together clickInside.
 *
 * @param element The element that uses the action, should not be passed.
 *
 * @param toggle The element that toggle the class.
 *
 * @returns Nothing, just remove Event Listenner.
 */

export function clickOutside(element: Element, toggle?: Element) {
    function onClick(event: any) {
        if ((!element.contains(event.target)) && (!toggle?.contains(event.target))) {
            const item: Element = element

            item.classList.remove(CLASS_NAME)
        }
    }

    document.body.addEventListener('click', onClick, true)

    return {
        destroy() {
            document.body.removeEventListener('click', onClick, true)
        }
    }
}
