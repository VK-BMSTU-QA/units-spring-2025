import { useProducts } from '../useProducts';
import { renderHook } from '@testing-library/react';

describe('test useProducts hook', () => {
    it('should return products list', () => {
        const renderedHook = renderHook(() => useProducts()); 
        expect(renderedHook.result.current.length).toBeGreaterThan(0);
    });

    it('should return the same product list every time', () => {
        const renderedHook = renderHook(() => useProducts()); 
        const prev = renderedHook.result.current;
        renderedHook.rerender();
        expect(renderedHook.result.current).toEqual(prev);
    });
});
