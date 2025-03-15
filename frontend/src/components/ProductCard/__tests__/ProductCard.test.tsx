import { cleanup, render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from '../ProductCard';
import type { Product } from '../../../types';

jest.mock('../../../utils', () => {
    return {
        getPrice: jest.fn(() => '999 $'),
    }
})

const product: Product = {
    id: 1,
    name: 'IPhone 14 Pro',
    description: 'Latest iphone, buy it now',
    price: 999,
    priceSymbol: '$',
    category: 'Электроника',
    imgUrl: '/iphone.png',
}

describe('testing product card component', () => {
    beforeEach(() => {
        jest.clearAllMocks()
    });
    afterEach(cleanup);

    it('renders', () => {
        const { asFragment } = render(
            <ProductCard
                {...product}
            />
        );
        expect(asFragment()).toMatchSnapshot();
    })

    it('uses getPrice to format price', () => {
        const { getPrice } = jest.requireMock('../../../utils');
        const rendered = render(
            <ProductCard
                {...product}
            />
        );

        expect(getPrice).toHaveBeenCalledTimes(1);
        expect(getPrice).toHaveBeenLastCalledWith(product.price, product.priceSymbol);
        expect(getPrice).toHaveReturnedWith('999 $');
        expect(rendered.getByText('999 $')).toBeInTheDocument();
    })

    it('renders product card image if it is provided', () => {
        const rendered = render(
            <ProductCard
                {...product}
            />
        );

        expect(rendered.container.querySelector('.product-card__image')).toBeInTheDocument();
        expect(rendered.container.querySelectorAll('.product-card__image').length).toBe(1);
        const imgElement = rendered.container.querySelector('.product-card__image') as HTMLImageElement;
        expect(new URL(imgElement.src).pathname).toBe(product.imgUrl);
        expect(imgElement.alt).toBe(product.name);
    })

    it('does not render product card image if it is not provided', () => {
        const rendered = render(
            // not using {...product} here because we need to pass null refUrl
            <ProductCard
                id={product.id}
                name={product.name}
                description={product.description}
                price={product.price}
                priceSymbol={product.priceSymbol}
                category={product.category}
            />
        );

        expect(rendered.container.querySelector('.product-card__image')).not.toBeInTheDocument();
    })

})
