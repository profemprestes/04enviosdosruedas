# Documentación Completa y Código Autocontenido: Página Principal (Home)

> **Ruta URL:** `/`  
> **Archivo de Página:** `src/app/page.tsx`  
> **Nota de Portabilidad:** Este documento incluye todo el código fuente de la página, sus componentes específicos, la estructura compartida del Layout (Header, Footer, Nav, CSS) y las constantes de negocio para permitir la generación de mockups HTML independientes sin depender del directorio `@src`.

---

## 1. Código Fuente de la Página (`src/app/page.tsx`)

```tsx
import type { Metadata } from 'next';
import dynamic from 'next/dynamic';
import HeroAnimado from '@/components/home/HeroAnimado';
import SegmentosHome from '@/components/home/SegmentosHome';
import ServicesOverview from '@/components/home/ServicesOverview';
import EmprendedoresHome from '@/components/home/EmprendedoresHome';
import CtaSection from '@/components/home/CtaSection';
import SocialProofSection from '@/components/home/SocialProofSection';

const LogisticaNetworkCanvas = dynamic(() => import('@/components/home/LogisticaNetworkCanvas'));

export const metadata: Metadata = {
  alternates: {
    canonical: '/',
  },
};

export default function HomePage() {
  return (
    <div id="home-page-container" className="bg-brand-white text-brand-ink selection:bg-brand-yellow selection:text-brand-blue overflow-x-hidden">
      <HeroAnimado />

      <SegmentosHome />

      <section 
        className="relative bg-brand-blue py-20 overflow-hidden" 
        aria-labelledby="services-section-title"
      >
        <LogisticaNetworkCanvas />
        <div className="absolute inset-0 bg-[radial-gradient(circle_at_30%_20%,rgba(255,255,255,0.08),transparent_60%)] pointer-events-none" />
        <div className="relative z-10 mx-auto max-w-[1280px] px-6 lg:px-8">
          <div className="max-w-180 mb-12">
            <div className="font-subheading text-[12px] tracking-mega uppercase text-brand-yellow">Nuestros Servicios</div>
            <h2 
              id="services-section-title"
              className="mt-4 font-display text-[clamp(2rem,4vw,2.75rem)] leading-[0.9] tracking-[-0.03em] uppercase text-white"
            >
              Conectamos Mar del Plata de punta a punta
            </h2>
          </div>
        </div>
        <ServicesOverview />
      </section>

      <EmprendedoresHome />
      <SocialProofSection />
      <CtaSection />
    </div>
  );
}

```

---

## 2. Componentes Específicos Importados por esta Página

### Componente: `src/components/home/HeroAnimado.tsx`

```tsx
import Image from 'next/image';
import { ArrowRight, MapPin, Zap } from 'lucide-react';
import { CTANestedPill } from '@/components/ui/CTANestedPill';
import { Knockout } from '@/components/ui/Knockout';
import Badge from '@/components/ui/Badge';
import HeroProceduralBackground from '@/components/ui/HeroProceduralBackground';

/**
 * Hero de inicio — concepto "mapa en vivo".
 *
 * La promesa de la casa es cobertura, así que la imagen principal no es una
 * foto de repartidor sino el mapa: un pin con anillos que salen hacia afuera y
 * dos fichas ancladas al barrio real. Los anillos se apagan con movimiento
 * reducido y arrancan invisibles hacia el final, así que sin animación el
 * bloque se ve limpio, no con tres círculos encima del pin.
 *
 * Abajo, el ticker repite los diferenciales. Va duplicado en el DOM y se
 * desplaza -50%: el bucle es invisible porque la segunda copia es idéntica.
 * Es `aria-hidden` y el texto real vive en un `sr-only`, para que un lector de
 * pantalla no lea la lista dos veces.
 */

/** Diferenciales del ticker. La lista se repite dos veces para que el bucle no se vea. */
const diferenciales = [
  'Envíos en el día',
  'Flota propia',
  'Cero tercerización',
  'Todo Mar del Plata',
  'Retiro en tu local',
];

/** Ficha sobre el mapa: dato duro arriba, barrio abajo. */
const fichas = [
  {
    id: 'base',
    posicion: 'left-[-4%] bottom-[14%]',
    tono: 'bg-white text-brand-blue-500',
    titulo: 'Base Friuli 1972',
    detalle: 'Mar del Plata',
  },
  {
    id: 'entrega',
    posicion: 'right-[-2%] top-[10%]',
    tono: 'bg-brand-yellow-500 text-brand-blue-500',
    titulo: 'Entrega en el día',
    detalle: 'en todo MDQ',
  },
] as const;

export default function HeroAnimado() {
  return (
    <section
      id="hero-animado"
      aria-label="Mensajería urbana y logística de última milla en todo Mar del Plata"
      className="relative isolate flex min-h-[90dvh] w-full flex-col overflow-hidden bg-brand-blue-500 text-white"
    >
      <HeroProceduralBackground variant="express" tone="blue" />

      <div className="relative z-10 mx-auto flex w-full max-w-7xl flex-1 items-center px-6 py-14 sm:py-20 lg:px-8 lg:py-24">
        <div className="grid w-full grid-cols-1 items-center gap-12 lg:grid-cols-12 lg:gap-14">
          {/* COPY 7 — nunca centrado en desktop. */}
          <div className="space-y-6 text-center sm:space-y-7 lg:col-span-7 lg:text-left">
            <Badge
              variant="accent"
              size="lg"
              className="-rotate-1"
              icon={<Zap className="h-4 w-4" aria-hidden="true" />}
            >
              Flota propia · Todo Mar del Plata
            </Badge>

            {/* Slogan del dueño (2026-09-29). El prototipo propone "Mensajería y
                logística e-commerce en Mar del Plata" como H1, pero eso es
                texto de diseño, no una frase del dueño: se queda como bajada.
                Las palabras del dueño no se reemplazan por las del mock. */}
            <h1 className="text-balance font-display text-4xl uppercase leading-[0.92] tracking-[-0.03em] text-white sm:text-5xl lg:text-6xl xl:text-7xl">
              <span className="block">El motor de tu</span>
              <Knockout className="whitespace-nowrap">última milla</Knockout>
              <span className="block">Somos la solución a tus envíos</span>
            </h1>

            <p className="mx-auto max-w-[56ch] text-pretty font-sans text-base font-light leading-relaxed text-white/85 sm:text-lg lg:mx-0">
              Mensajería y logística e-commerce en Mar del Plata: envíos en el día con motos
              propias. Llegamos a toda la ciudad y los repartidores son nuestros, sin tercerizar.
            </p>

            <div className="flex flex-col items-center justify-center gap-4 pt-1 sm:flex-row sm:gap-6 lg:justify-start">
              <CTANestedPill
                href="/cotizar"
                id="hero-cta-cotizar"
                variant="primary"
                size="large"
                className="focus-visible:ring-2 focus-visible:ring-brand-yellow-500 focus-visible:ring-offset-2 focus-visible:ring-offset-brand-blue-500"
              >
                Cotizá tu envío
              </CTANestedPill>
              <a
                href="/servicios"
                className="inline-flex min-h-11 items-center gap-2 rounded-md font-subheading text-sm uppercase tracking-wider text-white underline decoration-brand-yellow-500 decoration-2 underline-offset-4 transition-colors hover:text-brand-yellow-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 focus-visible:ring-offset-2 focus-visible:ring-offset-brand-blue-500 sm:text-base"
              >
                Ver servicios
                <ArrowRight className="h-4 w-4 shrink-0" aria-hidden="true" />
              </a>
            </div>
          </div>

          {/* MAPA 5 — pin + anillos + dos fichas ancladas. */}
          <div className="lg:col-span-5">
            <div className="relative mx-auto aspect-square w-full max-w-115">
              {/* Anillos: el `--delay` escalona el arranque para que el pulso sea continuo. */}
              <span
                aria-hidden="true"
                className="animate-pulse-ring absolute left-1/2 top-[44%] aspect-square w-[30%] -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-brand-yellow-500/60"
              />
              <span
                aria-hidden="true"
                className="animate-pulse-ring absolute left-1/2 top-[44%] aspect-square w-[30%] -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-brand-yellow-500/60 [animation-delay:1.06s]"
              />
              <span
                aria-hidden="true"
                className="animate-pulse-ring absolute left-1/2 top-[44%] aspect-square w-[30%] -translate-x-1/2 -translate-y-1/2 rounded-full border-2 border-brand-yellow-500/60 [animation-delay:2.13s]"
              />

              <Image
                src="/heroes/inicio-mapa.webp"
                alt="Pin de Envíos DosRuedas sobre un mapa isométrico de Mar del Plata con una ruta amarilla"
                width={560}
                height={560}
                priority
                sizes="(min-width: 1024px) 460px, 92vw"
                className="relative z-2 h-auto w-full drop-shadow-[0_24px_40px_rgba(255,255,255,0.12)]"
              />

              {fichas.map((ficha) => (
                <div
                  key={ficha.id}
                  className={`absolute z-3 inline-flex items-center gap-2 rounded-xl px-3 py-2.5 shadow-[0_12px_30px_rgba(9,80,246,0.25)] ${ficha.posicion} ${ficha.tono}`}
                >
                  <MapPin className="h-4 w-4 shrink-0" aria-hidden="true" />
                  <span className="font-mono text-2xs font-medium leading-tight">
                    <b className="block font-subheading text-xs uppercase tracking-wider">
                      {ficha.titulo}
                    </b>
                    {ficha.detalle}
                  </span>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>

      {/* Ticker de diferenciales. Duplicado y desplazado -50% para que el bucle no se note. */}
      <div className="relative z-10 border-t border-white/18 bg-white/6">
        <h2 className="sr-only">Diferenciales de Envíos DosRuedas</h2>
        <ul className="sr-only">
          {diferenciales.map((d) => (
            <li key={`sr-${d}`}>{d}</li>
          ))}
        </ul>
        <div
          aria-hidden="true"
          className="animate-marquee-left flex w-max items-center py-3.5"
        >
          {[0, 1].map((copia) => (
            <ul key={copia} className="flex shrink-0 items-center">
              {diferenciales.map((d) => (
                <li
                  key={`${copia}-${d}`}
                  className="flex items-center gap-9 whitespace-nowrap px-4.5 font-subheading text-base uppercase tracking-[0.08em] text-white sm:text-[17px]"
                >
                  {d}
                  <span className="h-1.75 w-1.75 rotate-45 rounded-xs bg-brand-yellow-500" />
                </li>
              ))}
            </ul>
          ))}
        </div>
      </div>
    </section>
  );
}

```

### Componente: `src/components/ui/CTANestedPill.tsx`

```tsx
'use client';

import React from 'react';
import Link from 'next/link';
import { ArrowRight } from 'lucide-react';
import { cn } from '@/lib/utils';
import { trackAnalytics } from '@/lib/analytics';

export type CTANestedPillVariant = 'primary' | 'blue' | 'elevated' | 'outline' | 'ghost';
export type CTANestedPillSize = 'compact' | 'default' | 'large' | 'lg';

export interface CTANestedPillProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  children: React.ReactNode;
  href?: string;
  variant?: CTANestedPillVariant;
  size?: CTANestedPillSize;
  icon?: React.ReactNode;
  iconPosition?: 'left' | 'right';
  className?: string;
  iconClassName?: string;
  target?: string;
  rel?: string;
}

/**
 * CTANestedPill Component
 * Standardized nested pill CTA interactive element (Button or Link).
 * Follows DESIGN.md specifications:
 * - Rounded-full, font-subheading, uppercase, tracking-wider, font-bold
 * - Embedded circular icon chip (w-8 h-8) with smooth hover translation
 * - Variants: --primary (yellow), --blue (para fondos amarillos), --elevated (white), --outline, --ghost
 */
export const CTANestedPill = React.forwardRef<HTMLButtonElement | HTMLAnchorElement, CTANestedPillProps>(
  (
    {
      children,
      href,
      variant = 'primary',
      size = 'default',
      icon,
      iconPosition = 'right',
      className,
      iconClassName,
      target,
      rel,
      disabled,
      ...buttonProps
    },
    ref
  ) => {
    const baseStyles =
      'cta-nested-pill group inline-flex items-center justify-between gap-3 rounded-full font-subheading uppercase tracking-wider font-bold transition-all duration-200 cursor-pointer focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-blue-500 focus-visible:ring-offset-2 select-none border';

    const normalizedSize = size === 'lg' ? 'large' : size;

    const sizeStyles = {
      compact: 'px-4 py-1.5 text-xs min-h-9',
      default: 'px-5 py-2 text-sm min-h-11',
      large: 'px-8 py-3 text-base min-h-13',
    }[normalizedSize];

    const variantStyles = {
      primary:
        'bg-brand-yellow-500 text-brand-blue-500 border-brand-yellow-500 shadow-accent-sm hover:shadow-cta-glow hover:bg-brand-yellow-400 active:scale-98 active:translate-y-px',
      // Para fondos amarillos (#FFEC01): azul de marca, texto blanco, chip amarillo.
      blue: 'bg-brand-blue-500 text-white border-brand-blue-500 shadow-[0_0_24px_rgba(9,80,246,0.28)] hover:bg-brand-blue-500 hover:border-brand-blue-500 active:scale-98 active:translate-y-px',
      elevated:
        'bg-white text-brand-blue-500 border-brand-blue-100 shadow-elevated hover:shadow-hover-lift hover:border-brand-blue-300 hover:text-brand-blue-500 active:scale-98',
      outline:
        'bg-transparent text-brand-blue-500 border-2 border-brand-blue-500 hover:bg-brand-blue-50 active:scale-98',
      ghost:
        'bg-transparent text-brand-blue-500 border-transparent hover:bg-brand-blue-50 active:scale-98',
    }[variant];

    const iconChipBase =
      'cta-nested-icon w-8 h-8 rounded-full flex items-center justify-center shrink-0 transition-all duration-200';

    const iconChipVariantStyles = {
      primary:
        'bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-brand-yellow-500 group-hover:translate-x-1',
      blue: 'bg-brand-yellow-500 text-brand-blue-500 group-hover:bg-brand-yellow-400 group-hover:translate-x-1',
      elevated:
        'bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-white group-hover:translate-x-1',
      outline:
        'bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-white group-hover:translate-x-1',
      ghost:
        'bg-transparent text-brand-blue-500 group-hover:bg-brand-blue-500 group-hover:text-white group-hover:translate-x-1',
    }[variant];

    const defaultIcon = <ArrowRight className="w-4 h-4" />;
    const renderedIcon = icon !== undefined ? icon : defaultIcon;

    const disabledStyles = disabled ? 'opacity-50 cursor-not-allowed pointer-events-none' : '';

    const combinedClassName = cn(
      baseStyles,
      sizeStyles,
      variantStyles,
      disabledStyles,
      className
    );

    const iconContent = (
      <span className={cn(iconChipBase, iconChipVariantStyles, iconClassName)}>
        {renderedIcon}
      </span>
    );

    const content = (
      <>
        {iconPosition === 'left' && iconContent}
        <span className="truncate">{children}</span>
        {iconPosition === 'right' && iconContent}
      </>
    );

    const handleClick = (e: React.MouseEvent<HTMLAnchorElement | HTMLButtonElement>) => {
      if (href && (href.includes('wa.me') || href.includes('whatsapp.com'))) {
        trackAnalytics.whatsappClick('cta_pill', typeof children === 'string' ? children : undefined);
      } else if (buttonProps.id || typeof children === 'string') {
        trackAnalytics.ctaClick(buttonProps.id || 'cta_pill', typeof children === 'string' ? children : 'cta');
      }
      if (buttonProps.onClick) {
        buttonProps.onClick(e as React.MouseEvent<HTMLButtonElement>);
      }
    };

    if (href && !disabled) {
      return (
        <Link
          href={href}
          ref={ref as React.Ref<HTMLAnchorElement>}
          className={combinedClassName}
          target={target}
          rel={rel}
          onClick={handleClick}
        >
          {content}
        </Link>
      );
    }

    return (
      <button
        ref={ref as React.Ref<HTMLButtonElement>}
        type={buttonProps.type || 'button'}
        disabled={disabled}
        className={combinedClassName}
        {...buttonProps}
        onClick={handleClick}
      >
        {content}
      </button>
    );
  }
);

CTANestedPill.displayName = 'CTANestedPill';

export default CTANestedPill;

```

### Componente: `src/components/ui/Knockout.tsx`

```tsx
import React from 'react';
import { cn } from '@/lib/utils';

export type KnockoutTone = 'yellow' | 'blue';

export interface KnockoutProps extends React.HTMLAttributes<HTMLSpanElement> {
  /** `yellow` sobre fondo azul (por defecto). `blue` sobre fondo amarillo. */
  tone?: KnockoutTone;
  children: React.ReactNode;
}

/**
 * Knockout — cápsula rotada que remata palabras clave del H1.
 *
 * Reglas de marca:
 * - Solo dos tonos: amarillo sobre azul, azul sobre amarillo.
 * - Nada más oscuro que `--color-brand-blue-500` (#0950F6), tampoco en el glow.
 * - Contraste AA en ambos sentidos (4.94:1).
 * - Server Component puro (sin hooks, sin motion): usable en cualquier hero.
 *
 * Sustituye a los `<span className="bg-[#FFEC01] text-[#0950F6] … -rotate-1">`
 * sueltos que estaban duplicados hero por hero.
 */
const toneStyles: Record<KnockoutTone, string> = {
  yellow: 'bg-brand-yellow-500 text-brand-blue-500 shadow-[0_0_28px_rgba(255,236,1,0.45)]',
  blue: 'bg-brand-blue-500 text-white shadow-[0_0_24px_rgba(9,80,246,0.28)]',
};

export function Knockout({ tone = 'yellow', className, children, ...rest }: KnockoutProps) {
  return (
    <span
      className={cn(
        'inline-block -rotate-1 rounded-full px-3 py-1 my-1 font-display uppercase leading-[1.1] tracking-[-0.02em] align-baseline',
        toneStyles[tone],
        className
      )}
      {...rest}
    >
      {children}
    </span>
  );
}

export default Knockout;

```

### Componente: `src/components/ui/Badge.tsx`

```tsx
'use client';

import React from 'react';
import { cn } from '@/lib/utils';

export type BadgeVariant =
  | 'urgent'
  | 'secure'
  | 'economic'
  | 'flex'
  | 'neutral'
  | 'outline'
  | 'primary'
  | 'accent';

export type BadgeSize = 'sm' | 'md' | 'lg';

export interface BadgeProps extends React.HTMLAttributes<HTMLSpanElement> {
  children: React.ReactNode;
  variant?: BadgeVariant;
  size?: BadgeSize;
  icon?: React.ReactNode;
  rounded?: 'full' | 'lg' | 'md';
  className?: string;
}

/**
 * Badge Component
 * Official badge pill system for statuses, trust indicators, and service types.
 * Follows DESIGN.md specifications:
 * - font-subheading, text-label, uppercase, tracking-wider, font-bold
 * - rounded-full or rounded-lg, padding var(--space-1) var(--space-2), border
 */
export const Badge: React.FC<BadgeProps> = ({
  children,
  variant = 'neutral',
  size = 'md',
  icon,
  rounded = 'full',
  className,
  ...props
}) => {
  const baseStyles =
    'inline-flex items-center gap-1.5 font-subheading uppercase tracking-wider font-bold border transition-colors select-none';

  const roundedStyles = {
    full: 'rounded-full',
    lg: 'rounded-lg',
    md: 'rounded-md',
  }[rounded];

  const sizeStyles = {
    sm: 'px-2 py-0.5 text-2xs leading-tight',
    md: 'px-3 py-1 text-xs leading-tight',
    lg: 'px-4 py-1.5 text-sm leading-tight',
  }[size];

  const variantStyles = {
    urgent:
      'bg-brand-yellow-500 text-brand-blue-500 border-brand-yellow-400 shadow-accent-sm',
    secure: 'bg-brand-blue-50 text-brand-blue-500 border-brand-blue-200',
    economic: 'bg-brand-blue-50 text-brand-blue-500 border-brand-blue-200',
    flex: 'bg-brand-yellow-100 text-brand-blue-500 border-brand-yellow-200',
    neutral: 'bg-white text-brand-blue-500 border-brand-blue-100 shadow-sm',
    outline: 'bg-transparent text-brand-blue-500 border-brand-blue-500',
    primary: 'bg-brand-blue-500 text-white border-brand-blue-500',
    accent:
      'bg-brand-yellow-500 text-brand-blue-500 border-brand-yellow-500 shadow-accent-sm',
  }[variant];

  return (
    <span
      className={cn(baseStyles, roundedStyles, sizeStyles, variantStyles, className)}
      {...props}
    >
      {icon && <span className="shrink-0">{icon}</span>}
      <span>{children}</span>
    </span>
  );
};

export default Badge;

```

### Componente: `src/components/ui/HeroProceduralBackground.tsx`

```tsx
import React from 'react';

export interface HeroProceduralBackgroundProps {
  variant?: 'express' | 'lowcost' | 'flex' | '3pl' | 'community' | 'contact' | 'default';
  /**
   * Eje tonal del fondo. `blue` (por defecto) es el azul de marca #0950F6 con
   * grilla punteada blanca; `yellow` es el amarillo vial #FFEC01 SIN gradiente,
   * con grilla azul punteada al 5% y un halo blanco suave encima.
   * En ambos tonos nada puede ser más oscuro que #0950F6.
   */
  tone?: 'blue' | 'yellow';
  className?: string;
}

/**
 * Fondo procedural de hero. Server Component: el gate de `prefers-reduced-motion`
 * es CSS (`motion-safe:`), no `useReducedMotion()`, para no romper el hydration —
 * `useReducedMotion()` devuelve `false` en el servidor y el valor real en el cliente.
 * 
 * Gradiente canónico Max (Ajuste #0950F6): linear-gradient(135deg, #0950F6 0%, #0950F6 55%, #3570F8 100%)
 * Halos con rgba(9,80,246,α) y rgba(255,236,1,α) — NUNCA rgba(6,54,165,…) ni rgba(0,39,124,…)
 */
export default function HeroProceduralBackground({
  variant = 'default',
  tone = 'blue',
  className = '',
}: HeroProceduralBackgroundProps) {
  const isYellow = tone === 'yellow';
  const accent = isYellow ? 'var(--color-brand-blue-500)' : 'var(--color-brand-yellow-500)';
  const softAccent = isYellow ? 'var(--color-brand-blue-500)' : 'var(--color-brand-blue-300)';
  const white = isYellow ? 'var(--color-brand-blue-500)' : 'var(--color-white)';
  const gridOpacity = isYellow ? 0.05 : 0.07;
  const artOpacity = isYellow ? 0.14 : 0.2;

  // Gradiente canónico Max: #0950F6 → #0950F6 → #3570F8 (nada más oscuro que #0950F6)
  const canonicalGradient = 'linear-gradient(135deg, #0950F6 0%, #0950F6 55%, #3570F8 100%)';

  return (
    <div
      className={`absolute inset-0 pointer-events-none select-none overflow-hidden ${className}`}
    >
      {isYellow ? (
        <>
          {/* Tono amarillo: base plana, sin gradiente. */}
          <div className="absolute inset-0 bg-brand-yellow-500" />
          <div
            className="absolute inset-x-0 top-0 h-[70%]"
            style={{
              background:
                'radial-gradient(ellipse at 50% 0%, rgba(255,255,255,0.55) 0%, rgba(255,255,255,0) 70%)',
            }}
          />
        </>
      ) : (
        <>
          {/* 1. Gradiente base canónico Max (Ajuste #0950F6) */}
          <div
            className="absolute inset-0"
            style={{ background: canonicalGradient }}
          />

          {/* 2. Procedural Dynamic Radial Highlights (CSS Glows) — Todos teñidos con brand colors */}
          <div
            className="absolute -top-32 -left-32 w-125 h-125 rounded-full pointer-events-none"
            style={{
              background:
                'radial-gradient(circle, rgba(9,80,246,0.35) 0%, rgba(9,80,246,0.18) 50%, transparent 70%)',
              filter: 'blur(80px)',
            }}
          />

          <div
            className="absolute top-1/4 -right-32 w-150 h-150 rounded-full pointer-events-none"
            style={{
              background:
                variant === 'express' || variant === 'lowcost'
                  ? 'radial-gradient(circle, rgba(255,236,1,0.22) 0%, rgba(255,236,1,0.06) 45%, transparent 70%)'
                  : 'radial-gradient(circle, rgba(255,236,1,0.16) 0%, rgba(9,80,246,0.12) 50%, transparent 70%)',
              filter: 'blur(90px)',
            }}
          />

          <div
            className="absolute -bottom-40 left-1/3 w-137.5 h-137.5 rounded-full pointer-events-none"
            style={{
              background: 'radial-gradient(circle, rgba(9,80,246,0.4) 0%, transparent 70%)',
              filter: 'blur(100px)',
            }}
          />
        </>
      )}

      {/* 3. Mathematical Vector Grid Topology (Pure SVG, 0 KB image) */}
      <svg
        className="absolute inset-0 w-full h-full"
        style={{ opacity: gridOpacity }}
        xmlns="http://www.w3.org/2000/svg"
      >
        <defs>
          <pattern
            id={`hero-procedural-grid-${tone}`}
            width="48"
            height="48"
            patternUnits="userSpaceOnUse"
          >
            <path
              d="M 48 0 L 0 0 0 48"
              fill="none"
              stroke={white}
              strokeWidth="0.75"
              strokeDasharray="2,6"
            />
            <circle cx="0" cy="0" r="1.5" fill={accent} />
          </pattern>
        </defs>
        <rect width="100%" height="100%" fill={`url(#hero-procedural-grid-${tone})`} />
      </svg>

      {/* 4. Variant-Specific Procedural Vector Graphics */}
      {variant === 'express' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Animated Speed & Logistics Arteries */}
          <path
            d="M -100 450 Q 400 200 900 380 T 1600 150"
            fill="none"
            stroke={accent}
            strokeWidth="2.5"
            strokeDasharray="12 16"
            className="motion-safe:animate-pulse"
          />
          <path
            d="M -100 300 Q 500 480 1000 250 T 1600 350"
            fill="none"
            stroke={softAccent}
            strokeWidth="1.5"
            strokeDasharray="8 12"
          />
          <circle cx="450" cy="240" r="4" fill={accent} />
          <circle cx="950" cy="360" r="5" fill={accent} />
        </svg>
      )}

      {variant === 'lowcost' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Concentric Cluster Routing Rings */}
          <circle cx="1100" cy="300" r="160" fill="none" stroke={accent} strokeWidth="1" strokeDasharray="4 8" />
          <circle cx="1100" cy="300" r="280" fill="none" stroke={softAccent} strokeWidth="1" strokeDasharray="6 12" />
          <circle cx="1100" cy="300" r="400" fill="none" stroke={white} strokeWidth="0.75" strokeDasharray="4 16" />
          <line x1="200" y1="300" x2="1100" y2="300" stroke={accent} strokeWidth="1.5" strokeDasharray="8 8" />
        </svg>
      )}

      {variant === 'flex' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Verified Dispatch Corridor Matrix */}
          <line x1="0" y1="180" x2="1440" y2="180" stroke={accent} strokeWidth="1.5" strokeDasharray="6 12" />
          <line x1="0" y1="420" x2="1440" y2="420" stroke={softAccent} strokeWidth="1" strokeDasharray="4 10" />
          <rect x="750" y="140" width="80" height="80" rx="16" fill="none" stroke={accent} strokeWidth="1.5" strokeDasharray="4 4" />
          <rect x="950" y="240" width="120" height="120" rx="24" fill="none" stroke={white} strokeWidth="1" strokeDasharray="6 8" />
        </svg>
      )}

      {variant === '3pl' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Inventory Hub Node Matrix */}
          <polygon points="900,150 1100,220 1000,420 800,350" fill="none" stroke={accent} strokeWidth="1.5" strokeDasharray="6 8" />
          <circle cx="900" cy="150" r="5" fill={accent} />
          <circle cx="1100" cy="220" r="5" fill={accent} />
          <circle cx="1000" cy="420" r="5" fill={accent} />
          <circle cx="800" cy="350" r="5" fill={accent} />
        </svg>
      )}

      {variant === 'community' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* Social Network Node Links */}
          <line x1="300" y1="200" x2="700" y2="150" stroke={softAccent} strokeWidth="1" />
          <line x1="700" y1="150" x2="1100" y2="280" stroke={accent} strokeWidth="1.5" />
          <line x1="1100" y1="280" x2="900" y2="480" stroke={softAccent} strokeWidth="1" />
          <line x1="900" y1="480" x2="500" y2="400" stroke={accent} strokeWidth="1" />
          <line x1="500" y1="400" x2="300" y2="200" stroke={softAccent} strokeWidth="1" />
        </svg>
      )}

      {variant === 'contact' && (
        <svg
          className="absolute inset-0 w-full h-full"
          style={{ opacity: artOpacity }}
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 1440 600"
          preserveAspectRatio="none"
        >
          {/* GPS Coordinate Beacon Radar */}
          <circle
            cx="1050"
            cy="320"
            r="80"
            fill="none"
            stroke={accent}
            strokeWidth="1.5"
            className="motion-safe:animate-ping [animation-duration:4s]"
          />
          <circle cx="1050" cy="320" r="180" fill="none" stroke={accent} strokeWidth="1" strokeDasharray="4 8" />
          <circle cx="1050" cy="320" r="300" fill="none" stroke={softAccent} strokeWidth="0.75" strokeDasharray="6 12" />
          <circle cx="1050" cy="320" r="6" fill={accent} />
        </svg>
      )}
    </div>
  );
}

```

### Componente: `src/components/home/SegmentosHome.tsx`

```tsx
'use client';

import React from 'react';
import Link from 'next/link';
import {
  ShoppingBag,
  Zap,
  Building2,
  PackageCheck,
  ArrowRight,
  Sparkles,
  Store,
} from 'lucide-react';
import { DoubleBezelCard } from '@/components/ui/DoubleBezelCard';
import {
  DROPOFF_DISCOUNT_PERCENT,
  EXPRESS_LEAD_TIME,
  FLEX_CUTOFF_TIME,
  LOWCOST_CUTOFF_TIME,
  LOWCOST_DELIVERY_DEADLINE,
  SAME_DAY_FIXED_PRICE,
} from '@/lib/promises';

const ars = (value: number) => `$${value.toLocaleString('es-AR')}`;

export default function SegmentosHome() {
  const segmentos = [
    {
      id: 'flex',
      tag: 'MERCADO LIBRE',
      title: '¿Vendés en Mercado Libre?',
      description: `Entregá en el mismo día con Mercado Envíos Flex en Mar del Plata urbana. Horario de corte ${FLEX_CUTOFF_TIME} y múltiples retiros para cuidar tu reputación.`,
      ctaText: 'Ver Solución Flex',
      href: '/servicios/enviosflex',
      icon: Zap,
      highlight: true,
    },
    {
      id: 'ecommerce',
      tag: 'E-COMMERCE 24HS / SAME-DAY',
      title: '¿Tenés tienda online con stock en depósito?',
      description: `E-Commerce 24hs: despacho garantizado en 24hs. E-Commerce Same-Day: entrega antes de 19hs con corte 13:00. Stock en Friuli 1972, picking QR, empaque incluido.`,
      ctaText: 'Ver planes E-Commerce',
      href: '/servicios',
      icon: Store,
      highlight: false,
    },
    {
      id: 'empresas',
      tag: 'COMERCIOS & EMPRESAS',
      title: '¿Tenés envíos diarios?',
      description: `Reparto económico programado para el día: pedís antes de las ${LOWCOST_CUTOFF_TIME} y se entrega antes de las ${LOWCOST_DELIVERY_DEADLINE}, sin franja horaria fija. Tarifa fija por distancia y remito digital.`,
      ctaText: 'Ver Paquetería LowCost',
      href: '/servicios/envios-lowcost',
      icon: Building2,
      highlight: false,
    },
    {
      id: 'urgente',
      tag: 'PARTICULARES & URGENTES',
      title: '¿Necesitás un envío ya?',
      description: `Cadetería prioritaria punto a punto en moto. Entregas prioritarias en el día con elección de franja horaria de 3 horas, pedido con ${EXPRESS_LEAD_TIME} mínima.`,
      ctaText: 'Cotizá tu Envío Express',
      href: '/cotizar',
      icon: PackageCheck,
      highlight: false,
    },
  ];

  return (
    <section 
      id="segmentos-home" 
      aria-labelledby="segmentos-home-title"
      className="py-20 bg-white relative z-10 border-b border-brand-blue-100/50"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 space-y-12">
        {/* Header */}
        <div className="text-center max-w-3xl mx-auto space-y-3">
          <div className="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-brand-yellow-500/15 border border-brand-yellow-500/30 text-brand-blue-500 text-xs font-subheading uppercase tracking-widest font-bold shadow-accent-sm">
            <Sparkles className="w-3.5 h-3.5 text-brand-blue-500" />
            <span>Elegí tu solución a medida</span>
          </div>
          <h2 id="segmentos-home-title" className="text-3xl sm:text-4xl lg:text-5xl font-display uppercase tracking-tight text-brand-blue-500">
            ¿CÓMO PODEMOS IMPULSAR TU LOGÍSTICA HOY?
          </h2>
          <p className="font-sans text-sm sm:text-base text-brand-blue-500 max-w-xl mx-auto leading-relaxed">
            Seleccioná tu tipo de negocio o necesidad y descubrí el servicio ideal diseñado para las calles de Mar del Plata.
          </p>
        </div>

        {/* Grid 4 Segmentos */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
          {segmentos.map((seg) => {
            const Icon = seg.icon;
            return (
              <DoubleBezelCard
                key={seg.id}
                outerClassName={
                  seg.highlight
                    ? 'bg-brand-yellow-500/20 border-2 border-brand-yellow-500 shadow-cta-glow hover:-translate-y-1'
                    : 'bg-brand-blue-50/80 border border-brand-blue-100 shadow-float hover:-translate-y-1'
                }
                innerClassName="h-full flex flex-col justify-between space-y-6"
              >
                <div className="space-y-4">
                  <div className="flex items-center justify-between">
                    <div className={`w-12 h-12 rounded-xl flex items-center justify-center shrink-0 ${
                      seg.highlight
                        ? 'bg-brand-yellow-500 text-brand-blue-500'
                        : 'bg-brand-blue-50 text-brand-blue-500'
                    }`}>
                      <Icon className="w-6 h-6" />
                    </div>
                    <span className="text-2xs font-mono uppercase font-bold tracking-wider px-2 py-0.5 rounded bg-brand-blue-50 text-brand-blue-500 border border-brand-blue-100">
                      {seg.tag}
                    </span>
                  </div>

                  <h3 className="font-display text-xl uppercase tracking-tight text-brand-blue-500 leading-snug">
                    {seg.title}
                  </h3>

                  <p className="font-sans text-xs sm:text-sm text-brand-blue-500 leading-relaxed font-normal">
                    {seg.description}
                  </p>
                </div>

                <div className="pt-4 border-t border-brand-blue-100">
                  <Link
                    href={seg.href}
                    className={`w-full min-h-11 px-4 py-2.5 rounded-full font-subheading text-xs uppercase tracking-wider font-bold flex items-center justify-between transition-all duration-200 cursor-pointer ${
                      seg.highlight
                        ? 'bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-500 shadow-accent-sm'
                        : 'bg-brand-blue-50 hover:bg-brand-blue-100 text-brand-blue-500 border border-brand-blue-200/60'
                    }`}
                  >
                    <span>{seg.ctaText}</span>
                    <ArrowRight className="w-4 h-4 ml-2 shrink-0" />
                  </Link>
                </div>
              </DoubleBezelCard>
            );
          })}
        </div>
      </div>
    </section>
  );
}

```

### Componente: `src/components/ui/DoubleBezelCard.tsx`

```tsx
'use client';

import React from 'react';
import { cn } from '@/lib/utils';

export interface DoubleBezelCardProps extends React.HTMLAttributes<HTMLDivElement> {
  children: React.ReactNode;
  className?: string;
  outerClassName?: string;
  innerClassName?: string;
  variant?: 'light' | 'dark';
  hoverEffect?: boolean;
}

/**
 * DoubleBezelCard Component
 * Signature Two-tier container system (outer bezel + inner card) for primary content.
 * Follows DESIGN.md specifications:
 * - Outer: bg-brand-blue-50/80, border-brand-blue-100, rounded-2xl (16px), p-2 (8px), shadow-float
 * - Inner: bg-white (or brand-blue-700 in dark variant), rounded-xl (12px), p-6, shadow-sm
 * - Hover: shadow-antigravity-deep, border-brand-blue-300
 */
export const DoubleBezelCard = React.forwardRef<HTMLDivElement, DoubleBezelCardProps>(
  (
    {
      children,
      className,
      outerClassName,
      innerClassName,
      variant = 'light',
      hoverEffect = true,
      ...props
    },
    ref
  ) => {
    const isDark = variant === 'dark';

    return (
      <div
        ref={ref}
        className={cn(
          'double-bezel-outer transition-all duration-300 rounded-2xl p-2 shadow-float',
          isDark
            ? 'bg-brand-blue-50/80 border border-brand-blue-100/80'
            : 'bg-brand-blue-50/80 border border-brand-blue-100',
          hoverEffect &&
            (isDark
              ? 'hover:shadow-antigravity-deep hover:border-brand-yellow-400/80'
              : 'hover:shadow-antigravity-deep hover:border-brand-blue-300'),
          outerClassName,
          className
        )}
        {...props}
      >
        <div
          className={cn(
            'double-bezel-inner rounded-xl p-6 shadow-sm overflow-hidden transition-colors duration-200',
            isDark
              ? 'bg-brand-blue-500 border border-white/10 text-white'
              : 'bg-white border border-brand-blue-50/50 text-brand-blue-500',
            innerClassName
          )}
        >
          {children}
        </div>
      </div>
    );
  }
);

DoubleBezelCard.displayName = 'DoubleBezelCard';

export default DoubleBezelCard;

```

### Componente: `src/components/home/ServicesOverview.tsx`

```tsx
'use client';

import React, { useState, useEffect, useRef, useCallback } from 'react';
import { motion, AnimatePresence, useReducedMotion } from 'motion/react';
import Image from 'next/image';
import { ChevronLeft, ChevronRight, Zap, Package, Truck, Warehouse, Info, X, MapPin, ShieldCheck } from 'lucide-react';
import {
  DROPOFF_DISCOUNT_PERCENT,
  EXPRESS_LEAD_TIME,
  EXPRESS_WINDOW_SHORT,
  FLEX_CUTOFF_TIME,
  LOWCOST_CUTOFF_TIME,
  LOWCOST_DELIVERY_DEADLINE,
  SAME_DAY_FIXED_PRICE,
  STANDARD_WEIGHT_KG,
} from '@/lib/promises';

const formatArs = (value: number) => `$${value.toLocaleString('es-AR')}`;

interface ServiceDetails {
  summary: string;
  features: string[];
  ctaText: string;
  ctaHref: string;
}

interface ServiceStats {
  time: string;
  price: string;
  weight: string;
}

interface ServiceItem {
  id: string;
  title: string;
  description: string;
  href: string;
  icon: React.ComponentType<{ className?: string }>;
  badge: string;
  city: string;
  founded: string;
  imageUrl: string;
  cardStyleCenter: string;
  cardStyleSide: string;
  textColor: string;
  titleColor: string;
  descColor: string;
  imgBlend: string;
  badgeStyle: string;
  statBoxStyle: string;
  statValStyle: string;
  statLabelStyle: string;
  hintColor: string;
  stats: ServiceStats;
  details: ServiceDetails;
}

export default function ServicesOverview() {
  const reduceMotion = useReducedMotion();
  const [activeIndex, setActiveIndex] = useState<number>(0);
  const [selectedService, setSelectedService] = useState<ServiceItem | null>(null);
  const [isAutoRotate, setIsAutoRotate] = useState<boolean>(true);
  const [isSmallScreen, setIsSmallScreen] = useState<boolean>(false);
  const carouselRef = useRef<HTMLDivElement>(null);

  // Bloquear scroll del body y cerrar con Escape mientras el modal está abierto
  useEffect(() => {
    if (!selectedService) return;
    const prevOverflow = document.body.style.overflow;
    document.body.style.overflow = 'hidden';
    const onKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') setSelectedService(null);
    };
    window.addEventListener('keydown', onKeyDown);
    return () => {
      document.body.style.overflow = prevOverflow;
      window.removeEventListener('keydown', onKeyDown);
    };
  }, [selectedService]);

  // Snappy spring configs
  const springConfigSnappy = { type: 'spring' as const, stiffness: 300, damping: 25 };
  const springConfigCarousel = { type: 'spring' as const, stiffness: 140, damping: 22 };

  const services: ServiceItem[] = [
    {
      id: 'express',
      title: 'Envíos Express',
      description: 'Mensajería en moto con franja horaria de 3 hs a elección.',
      href: '/servicios/envios-express',
      icon: Zap,
      badge: 'URGENTE',
      city: 'Todo Mar del Plata',
      founded: '+7 Años de Trayectoria',
      imageUrl: '/cards/fondo_express.webp',
      cardStyleCenter: 'border-brand-yellow-500 bg-linear-to-br from-brand-blue-500 to-brand-blue-500 shadow-cta-glow text-white',
      cardStyleSide: 'border-brand-blue-500/20 bg-brand-blue-500 text-white/90',
      textColor: 'text-white',
      titleColor: 'text-white group-hover:text-brand-yellow-500',
      descColor: 'text-brand-blue-50',
      imgBlend: 'opacity-25 mix-blend-overlay',
      badgeStyle: 'bg-brand-yellow-500 text-brand-blue-500 border-brand-yellow-400',
      statBoxStyle: 'bg-white/10 border border-white/10 text-white',
      statValStyle: 'text-brand-yellow-500',
      statLabelStyle: 'text-brand-blue-50',
      hintColor: 'text-brand-yellow-500',
      stats: {
        time: EXPRESS_WINDOW_SHORT,
        price: '$3.700 Base',
        weight: `Hasta ${STANDARD_WEIGHT_KG} kg`,
      },
      details: {
        summary: `Servicio de mensajería urbana con horario a elección, ideal para trámites urgentes, despacho de encomiendas y entrega de documentación. Coordinás la franja horaria que te conviene y se asigna un repartidor exclusivo para tu envío.`,
        features: [
          'Tarifa base de $3.700 hasta 3 km.',
          `Entrega en franja de 3 hs a elección, pedido con ${EXPRESS_LEAD_TIME} mínima.`,
          'Notificación automática de entrega por WhatsApp.'
        ],
        ctaText: 'COTIZÁ TU EXPRESS',
        ctaHref: '/cotizar'
      }
    },
    {
      id: 'lowcost',
      title: 'Envíos LowCost',
      description: 'Envíos económicos programados en el día, sin elección de horario.',
      href: '/servicios/envios-lowcost',
      icon: Package,
      badge: 'ECONÓMICO',
      city: 'Todo Gral. Pueyrredón',
      founded: 'Tarifa Fija Especial',
      imageUrl: '/cards/fondo_lowcost.webp',
      cardStyleCenter: 'border-brand-blue-500 bg-linear-to-br from-white to-brand-blue-50 shadow-[8px_8px_0px_rgba(9,80,246,0.2)] text-brand-blue-500',
      cardStyleSide: 'border-brand-blue-100 bg-white text-brand-blue-500',
      textColor: 'text-brand-blue-500',
      titleColor: 'text-brand-blue-500 group-hover:text-brand-blue-500',
      descColor: 'text-brand-blue-500',
      imgBlend: 'opacity-[0.15] grayscale mix-blend-multiply',
      badgeStyle: 'bg-brand-blue-500 text-brand-yellow-500 border-brand-blue-400',
      statBoxStyle: 'bg-brand-blue-50/80 border border-brand-blue-100 text-brand-blue-500',
      statValStyle: 'text-brand-blue-500',
      statLabelStyle: 'text-brand-blue-500',
      hintColor: 'text-brand-blue-500',
      stats: {
        time: 'Programado en el día',
        price: '$3.000 Base',
        weight: `Hasta ${STANDARD_WEIGHT_KG} kg`,
      },
      details: {
        summary: 'La alternativa ideal para comercios y e-commerce que buscan optimizar costos de envío. Es un reparto económico programado para el día, no un agrupamiento de tus propios envíos: lo pedís antes del corte y se entrega a lo largo de la jornada.',
        features: [
          'Tarifa base de $3.000 hasta 3 km.',
          `Pedí antes de las ${LOWCOST_CUTOFF_TIME} y se entrega antes de las ${LOWCOST_DELIVERY_DEADLINE}.`,
          'Sin elección de franja horaria: la tarifa más baja de la ciudad.'
        ],
        ctaText: 'PROBÁ EL LOWCOST',
        ctaHref: '/cotizar'
      }
    },
    {
      id: 'flex',
      title: 'Envíos Flex',
      description: 'Entregas en el día integradas para tus ventas de MercadoLibre.',
      href: '/servicios/enviosflex',
      icon: Truck,
      badge: 'MERCADOLIBRE FLEX',
      city: 'Mar del Plata urbana',
      founded: `Corte extendido ${FLEX_CUTOFF_TIME}`,
      imageUrl: '/cards/fondo_flex.webp',
      cardStyleCenter: 'border-brand-blue-500 bg-linear-to-br from-brand-yellow-500 to-brand-yellow-400 shadow-[8px_8px_0px_rgba(255,236,1,0.25)] text-brand-blue-500',
      cardStyleSide: 'border-brand-yellow-500/30 bg-brand-yellow-500 text-brand-blue-500',
      textColor: 'text-brand-blue-500',
      titleColor: 'text-brand-blue-500 group-hover:text-brand-blue-500',
      descColor: 'text-brand-blue-500',
      imgBlend: 'opacity-20 mix-blend-multiply',
      badgeStyle: 'bg-brand-blue-500 text-white border-brand-blue-500/30',
      statBoxStyle: 'bg-brand-yellow-500 border border-brand-blue-500/30 text-brand-blue-500',
      statValStyle: 'text-brand-blue-500',
      statLabelStyle: 'text-brand-blue-500',
      hintColor: 'text-brand-blue-500',
      stats: {
        time: 'En el día',
        price: 'Zonificado LowCost',
        weight: 'Apto Moto / Auto',
      },
      details: {
        summary: 'Habilitá Envíos Flex en tu cuenta de MercadoLibre y despachá todas tus ventas en el mismo día. Mejorá tu reputación y convertite en vendedor destacado con recolección gratuita.',
        features: [
          'Visitas bonificadas según tu volumen diario de entregas.',
          'Reparto coordinado antes de las 20:00 hs.',
          'Recolección a domicilio sin cargo extra por nuestro equipo.'
        ],
        ctaText: 'CONFIGURÁ FLEX',
        ctaHref: '/servicios/enviosflex'
      }
    },
    {
      id: '3pl',
      title: 'E-Commerce Same Day',
      description: 'Guardamos tu stock y lo despachamos el mismo día, o E-Commerce 24HS si lo necesitás al día siguiente.',
      href: '/servicios/deposito-fulfillment',
      icon: Warehouse,
      badge: 'E-COMMERCE',
      city: 'Depósito Friuli 1972',
      founded: 'Stock guardado',
      imageUrl: '/cards/fondo_emprendedores.webp',
      cardStyleCenter: 'border-brand-blue-500 bg-linear-to-br from-brand-blue-500 to-brand-blue-500 shadow-2xl text-white',
      cardStyleSide: 'border-brand-blue-500/20 bg-brand-blue-500 text-white/90',
      textColor: 'text-white',
      titleColor: 'text-white group-hover:text-brand-yellow-500',
      descColor: 'text-brand-blue-50',
      imgBlend: 'opacity-25 mix-blend-overlay',
      badgeStyle: 'bg-brand-blue-500 text-white border-brand-blue-500/30',
      statBoxStyle: 'bg-white/10 border border-white/10 text-white',
      statValStyle: 'text-brand-yellow-500',
      statLabelStyle: 'text-brand-blue-50',
      hintColor: 'text-brand-yellow-500',
      stats: {
        time: 'Same Day / 24 hs',
        price: `${formatArs(SAME_DAY_FIXED_PRICE)} fijo`,
        weight: 'Sin límite',
      },
      details: {
        summary: 'Almacená tus productos en nuestro depósito central de Friuli 1972 y olvidate del empaque y los despachos. Nosotros nos encargamos de todo el proceso logístico para que te dediques a vender.',
        features: [
          `E-Commerce Same Day con tarifa fija de ${formatArs(SAME_DAY_FIXED_PRICE)} a toda la ciudad.`,
          `E-Commerce 24HS con ${DROPOFF_DISCOUNT_PERCENT}% OFF si traés los envíos listos (DropOFF).`,
          'Control de stock digital por sistema QR/barras y picking con embalaje profesional.'
        ],
        ctaText: 'CONSULTÁ PLANES',
        ctaHref: '/servicios/deposito-fulfillment'
      }
    },
  ];

  const totalServices = services.length;
  const autoRotateIntervalRef = useRef<NodeJS.Timeout | null>(null);

  // Handle resize
  useEffect(() => {
    const handleResize = () => {
      setIsSmallScreen(window.innerWidth < 640);
    };
    handleResize();
    window.addEventListener('resize', handleResize);
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  // Auto-rotation with deterministic timing
  useEffect(() => {
    if (!isAutoRotate || reduceMotion || selectedService) {
      if (autoRotateIntervalRef.current) {
        clearInterval(autoRotateIntervalRef.current);
        autoRotateIntervalRef.current = null;
      }
      return;
    }

    autoRotateIntervalRef.current = setInterval(() => {
      setActiveIndex((prev) => (prev + 1) % totalServices);
    }, 4500);

    return () => {
      if (autoRotateIntervalRef.current) {
        clearInterval(autoRotateIntervalRef.current);
        autoRotateIntervalRef.current = null;
      }
    };
  }, [isAutoRotate, totalServices, reduceMotion, selectedService]);

  const handlePrev = useCallback(() => {
    setIsAutoRotate(false);
    setActiveIndex((prev) => (prev - 1 + totalServices) % totalServices);
  }, [totalServices]);

  const handleNext = useCallback(() => {
    setIsAutoRotate(false);
    setActiveIndex((prev) => (prev + 1) % totalServices);
  }, [totalServices]);

  // Keyboard navigation
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (selectedService) {
        if (e.key === 'Escape') setSelectedService(null);
        return;
      }
      if (e.key === 'ArrowLeft') {
        handlePrev();
      } else if (e.key === 'ArrowRight') {
        handleNext();
      }
    };

    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [handlePrev, handleNext, selectedService]);

  // Calculate card transforms using spring-based derived values
  const getCardTransform = (index: number) => {
    const offset = (index - activeIndex + totalServices / 2) % totalServices - totalServices / 2;
    const absOffset = Math.abs(offset);
    const isCenter = offset === 0;

    if (reduceMotion) {
      return {
        rotateY: 0,
        translateZ: 0,
        translateX: 0,
        opacity: isCenter ? 1 : 0,
        scale: isCenter ? 1 : 0.7,
        zIndex: isCenter ? totalServices : totalServices - absOffset,
      };
    }

    const rotateY = offset * -28;
    const translateZ = isCenter ? 120 : -absOffset * 180;
    const translateX = offset * (isSmallScreen ? 140 : 260);
    const opacity = isCenter ? 1 : Math.max(0.15, 1 - absOffset * 0.4);
    const scale = isCenter ? 1.05 : Math.max(0.65, 1 - absOffset * 0.18);

    return { rotateY, translateZ, translateX, opacity, scale, zIndex: totalServices - absOffset };
  };

  return (
    <section
      id="services-overview"
      aria-labelledby="services-overview-title"
      className="py-24 bg-brand-blue text-white relative overflow-hidden perspective-[2000px]"
      onMouseEnter={() => setIsAutoRotate(false)}
      onMouseLeave={() => !selectedService && setIsAutoRotate(true)}
    >
      {/* Background Decorative Asymmetric Glows */}
      <div className="absolute top-0 left-0 w-96 h-96 bg-brand-blue-500/10 rounded-full blur-3xl pointer-events-none" />
      <motion.div
        className="absolute bottom-0 right-0 w-125 h-125 bg-brand-yellow-500/5 rounded-full blur-3xl pointer-events-none"
        animate={reduceMotion ? {} : { scale: [1, 1.05, 1] }}
        transition={{ duration: 4, ease: 'easeInOut', repeat: Infinity }}
      />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        {/* Editorial Section Header with Viewport Entry */}
        <motion.div
          initial={{ opacity: 0, y: 30 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true, margin: '-50px' }}
          transition={{ type: 'spring', stiffness: 100, damping: 20 }}
          className="flex flex-col md:flex-row md:items-end justify-between mb-16 gap-6 border-b border-white/10 pb-8"
        >
          <div>
            <div className="px-4 py-1.5 bg-brand-blue-500 text-brand-yellow-400 rounded-full text-xs font-subheading font-bold tracking-widest inline-block uppercase shadow-glow-yellow mb-3 border border-brand-yellow-400/40">
              NUESTROS SERVICIOS
            </div>
            <h2 id="services-overview-title" className="font-display text-4xl sm:text-6xl uppercase text-white tracking-tight leading-none text-balance">
              SOLUCIONES LOGÍSTICAS <br />
              <span className="text-brand-yellow-400 drop-shadow-[0_2px_10px_rgba(255,241,46,0.35)] underline decoration-brand-blue-500 underline-offset-8">
                A TU MEDIDA
              </span>
            </h2>
          </div>

          <div className="flex items-center gap-4">
            <motion.button
              type="button"
              onClick={() => setIsAutoRotate(!isAutoRotate)}
              whileHover={reduceMotion ? undefined : { scale: 1.02 }}
              whileTap={reduceMotion ? undefined : { scale: 0.98 }}
              className={`px-4 py-2 rounded-full text-xs font-bold font-subheading tracking-wider border transition-colors cursor-pointer ${
                isAutoRotate
                  ? 'bg-brand-yellow-400 text-brand-blue-500 border-brand-yellow-400 shadow-glow-yellow'
                  : 'bg-white/10 text-white border-white/20 hover:bg-white/20'
              }`}
            >
              {isAutoRotate ? '⚡ ROTACIÓN AUTOMÁTICA' : 'ROTACIÓN PAUSADA'}
            </motion.button>

            <div className="flex items-center gap-2">
              <motion.button
                type="button"
                onClick={handlePrev}
                whileHover={reduceMotion ? undefined : { scale: 1.05 }}
                whileTap={reduceMotion ? undefined : { scale: 0.95 }}
                className="p-3 rounded-full bg-white/10 hover:bg-brand-yellow-500 hover:text-brand-blue-500 border border-white/20 cursor-pointer transition-colors"
                aria-label="Anterior Servicio"
              >
                <ChevronLeft className="w-5 h-5" />
              </motion.button>
              <motion.button
                type="button"
                onClick={handleNext}
                whileHover={reduceMotion ? undefined : { scale: 1.05 }}
                whileTap={reduceMotion ? undefined : { scale: 0.95 }}
                className="p-3 rounded-full bg-white/10 hover:bg-brand-yellow-500 hover:text-brand-blue-500 border border-white/20 cursor-pointer transition-colors"
                aria-label="Siguiente Servicio"
              >
                <ChevronRight className="w-5 h-5" />
              </motion.button>
            </div>
          </div>
        </motion.div>

        {/* 3D Tilted Card Carousel Container */}
        <div
          ref={carouselRef}
          className="relative h-125 sm:h-135 flex items-center justify-center my-8 transform-3d"
        >
          {services.map((service, index) => {
            const Icon = service.icon;
            const transform = getCardTransform(index);
            const isCenter = transform.opacity === 1;

            return (
              <motion.button
                key={service.id}
                type="button"
                onClick={() => {
                  if (isCenter) {
                    setSelectedService(service);
                  } else {
                    setActiveIndex(index);
                    setIsAutoRotate(false);
                  }
                }}
                className="absolute w-72.5 sm:w-87.5 h-110 sm:h-122.5 rounded-3xl cursor-pointer select-none group text-left focus-visible:outline-none focus-visible:ring-4 focus-visible:ring-brand-yellow-500 focus-visible:ring-offset-2 focus-visible:ring-offset-brand-ink"
                style={{
                  transformStyle: 'preserve-3d',
                  zIndex: transform.zIndex,
                  willChange: 'transform, opacity',
                }}
                animate={{
                  rotateY: transform.rotateY,
                  translateZ: transform.translateZ,
                  translateX: transform.translateX,
                  // Los cards laterales no se atenúan: el fade del ancestro (opacity < 1)
                  // degradaba el contraste de los chips (URGENTE/ECONÓMICO/LOGÍSTICA INTEGRAL)
                  // por debajo de AA 4.5. La profundidad se mantiene con rotateY/scale/translateZ.
                  opacity: reduceMotion ? transform.opacity : 1,
                  scale: transform.scale,
                }}
                transition={
                  reduceMotion
                    ? { duration: 0.01 }
                    : springConfigCarousel
                }
                whileHover={isCenter && !reduceMotion ? { scale: 1.02, transition: springConfigSnappy } : undefined}
              >
                {/* Card Structure with Color Block Themes */}
                <div
                  className={`w-full h-full rounded-3xl p-6 flex flex-col justify-between relative overflow-hidden border-4 shadow-2xl ${
                    isCenter ? service.cardStyleCenter : service.cardStyleSide
                  }`}
                >
                  {/* Background Image with Layer Blend */}
                  <div className="absolute inset-0 w-full h-full pointer-events-none select-none z-0">
                    <Image
                      src={service.imageUrl}
                      alt={service.title}
                      fill={true}
                      sizes="(max-width: 768px) 290px, 350px"
                      className={`object-cover ${service.imgBlend}`}
                    />
                    <div className="absolute inset-0 bg-linear-to-t from-brand-blue-500/80 via-brand-blue-500/20 to-transparent opacity-60" />
                  </div>

                  {/* Center Card Ambient Glow Overlay */}
                  {isCenter && (
                    <motion.div
                      className="absolute bottom-0 right-0 w-48 h-48 rounded-full blur-3xl pointer-events-none opacity-20 -mr-12 -mb-12"
                      style={{
                        backgroundColor: index === 3 ? 'var(--color-brand-blue-500)' : 'var(--color-brand-yellow-500)',
                      }}
                      animate={reduceMotion ? {} : { scale: [1, 1.08, 1], opacity: [0.15, 0.25, 0.15] }}
                      transition={{ duration: 3, ease: 'easeInOut', repeat: Infinity }}
                    />
                  )}

                  {/* Watermark Background Icon */}
                  <motion.div
                    className="absolute right-4 bottom-4 opacity-[0.06] pointer-events-none select-none"
                    animate={isCenter && !reduceMotion ? { rotate: [0, 2, -2, 0], scale: [1, 1.02, 1] } : {}}
                    transition={{ duration: 4, ease: 'easeInOut', repeat: Infinity }}
                  >
                    <Icon className="w-48 h-48" />
                  </motion.div>

                  {/* Top Badge Symbol & Serie Badge */}
                  <div className="relative z-10 flex items-center justify-between">
                    <motion.div
                      className="flex items-center gap-2.5"
                      whileHover={reduceMotion ? undefined : { scale: 1.05, transition: springConfigSnappy }}
                    >
                      <div className="p-3 bg-brand-yellow-500 text-brand-blue-500 rounded-xl shadow-[2px_2px_0px_var(--color-brand-blue-500)]">
                        <Icon className="h-5 w-5" />
                      </div>
                      <span className={`text-2xs font-bold font-subheading px-2.5 py-1 rounded-full border shadow-sm ${service.badgeStyle}`}>
                        {service.badge}
                      </span>
                    </motion.div>
                  </div>

                  {/* Middle Service Information */}
                  <div className="relative z-10 space-y-2 mt-auto">
                    <div className={`text-xs font-bold uppercase tracking-widest font-subheading flex items-center gap-1 ${service.hintColor}`}>
                      <MapPin className="w-3.5 h-3.5" />
                      {service.city}
                    </div>
                    <motion.h3
                      className={`font-display text-2xl sm:text-3xl uppercase leading-none text-balance ${service.titleColor}`}
                      whileHover={reduceMotion ? undefined : { x: 4, transition: springConfigSnappy }}
                    >
                      {service.title}
                    </motion.h3>
                    <p className={`text-xs line-clamp-2 leading-relaxed ${service.descColor}`}>
                      {service.description}
                    </p>
                  </div>

                  {/* Bottom Stats Grid & Callout */}
                  <div className="relative z-10 pt-4 border-t border-white/5 grid grid-cols-3 gap-2 text-center">
                    <div className={`p-2 rounded-xl backdrop-blur-sm ${service.statBoxStyle}`}>
                      <div className="text-sm font-bold font-subheading truncate">{service.stats.time}</div>
                      <div className={`text-2xs uppercase font-bold tracking-wider ${service.statLabelStyle}`}>ENTREGA</div>
                    </div>
                    <div className={`p-2 rounded-xl backdrop-blur-sm ${service.statBoxStyle}`}>
                      <div className="text-sm font-bold font-subheading truncate">{service.stats.price}</div>
                      <div className={`text-2xs uppercase font-bold tracking-wider ${service.statLabelStyle}`}>TARIFA</div>
                    </div>
                    <div className={`p-2 rounded-xl backdrop-blur-sm ${service.statBoxStyle}`}>
                      <div className="text-sm font-bold font-subheading truncate">{service.stats.weight}</div>
                      <div className={`text-2xs uppercase font-bold tracking-wider ${service.statLabelStyle}`}>PESO</div>
                    </div>
                  </div>

                  {/* Center Card Click Hint */}
                  {isCenter && (
                    <motion.div
                      className="relative z-10 mt-3 text-center"
                      animate={reduceMotion ? {} : { opacity: [1, 0.6, 1] }}
                      transition={{ duration: 2, ease: 'easeInOut', repeat: Infinity }}
                    >
                      <span className={`inline-flex items-center gap-1.5 text-xs font-bold font-subheading tracking-wider underline uppercase ${service.hintColor}`}>
                        <Info className="w-3.5 h-3.5" />
                        Mirá la Ficha Técnica
                      </span>
                    </motion.div>
                  )}
                </div>
              </motion.button>
            );
          })}
        </div>

        {/* Carousel Indicators */}
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          whileInView={{ opacity: 1, y: 0 }}
          viewport={{ once: true }}
          transition={{ type: 'spring', stiffness: 100, damping: 20, delay: 0.2 }}
          className="flex items-center justify-center gap-2 mt-8"
          role="group"
          aria-label="Navegación de servicios"
        >
          {services.map((service, i) => (
            <motion.button
              key={service.id}
              type="button"
              onClick={() => {
                setActiveIndex(i);
                setIsAutoRotate(false);
              }}
              aria-label={`Ir al servicio ${service.title}${i === activeIndex ? ', servicio actual' : ''}`}
              aria-current={i === activeIndex ? 'true' : 'false'}
              className={`min-w-11 min-h-11 flex items-center justify-center rounded-full cursor-pointer focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500`}
              whileHover={i !== activeIndex && !reduceMotion ? { scale: 1.2, transition: springConfigSnappy } : undefined}
              whileTap={reduceMotion ? undefined : { scale: 0.9 }}
            >
              <motion.span
                className={`h-2.5 rounded-full block ${
                  i === activeIndex ? 'bg-brand-yellow-500 shadow-cta-glow' : 'bg-white/30 hover:bg-white/60 border border-brand-blue-200'
                }`}
                animate={{ width: i === activeIndex ? '2.5rem' : '0.625rem' }}
                transition={springConfigSnappy}
              />
            </motion.button>
          ))}
        </motion.div>
      </div>

      {/* Interactive Modal for Selected Service Details */}
      <AnimatePresence>
        {selectedService && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            transition={{ duration: 0.2, ease: 'easeOut' }}
            className="fixed inset-0 z-50 bg-brand-blue-500/80 backdrop-blur-md flex items-center justify-center p-4 overscroll-contain overflow-y-auto"
            role="dialog"
            aria-modal="true"
            aria-labelledby="service-modal-title"
          >
            <motion.div
              initial={{ opacity: 0, scale: 0.95, y: 20 }}
              animate={{ opacity: 1, scale: 1, y: 0 }}
              exit={{ opacity: 0, scale: 0.95, y: 20 }}
              transition={{ type: 'spring', stiffness: 120, damping: 20 }}
              className="double-bezel-outer p-2 rounded-3xl bg-brand-blue-50/10 border border-brand-blue-100/20 max-w-2xl w-full"
            >
              <div className="double-bezel-inner bg-brand-blue-500 border border-brand-blue-500/20 rounded-2xl p-6 sm:p-8 text-white relative shadow-2xl space-y-6">
                {/* Close Modal Button */}
                <motion.button
                  type="button"
                  onClick={() => setSelectedService(null)}
                  whileHover={reduceMotion ? undefined : { scale: 1.1, rotate: 90, transition: springConfigSnappy }}
                  whileTap={reduceMotion ? undefined : { scale: 0.9 }}
                  className="absolute top-4 right-4 p-2 rounded-full bg-white/10 hover:bg-brand-yellow-500 hover:text-brand-blue-500 transition-colors cursor-pointer z-20"
                  aria-label="Cerrar ficha técnica"
                >
                  <X className="w-5 h-5" />
                </motion.button>

                {/* Modal Header */}
                <div className="flex items-center gap-4 text-left">
                  <div className="p-4 bg-brand-yellow-500 text-brand-blue-500 rounded-2xl shadow-[3px_3px_0px_var(--color-brand-blue-500)]">
                    {React.createElement(selectedService.icon, { className: "w-8 h-8" })}
                  </div>
                  <div>
                    <span className="text-2xs font-bold text-brand-yellow-500 font-subheading tracking-widest uppercase">
                      {selectedService.founded} • {selectedService.city}
                    </span>
                    <h3 id="service-modal-title" className="font-display text-3xl sm:text-4xl uppercase text-balance mt-0.5">
                      {selectedService.title}
                    </h3>
                  </div>
                </div>

                {/* Description & Features Box */}
                <div className="space-y-4 bg-brand-blue-500 p-5 rounded-2xl border border-brand-blue-500/10 text-left">
                  <p className="text-sm sm:text-base leading-relaxed text-brand-blue-50 font-sans">
                    {selectedService.details.summary}
                  </p>

                  <div className="space-y-2 pt-2 border-t border-brand-blue-500/10">
                    <span className="text-xs font-subheading text-brand-yellow-500 font-bold uppercase tracking-wider block">Beneficios Clave:</span>
                    {selectedService.details.features.map((feat: string, fIdx: number) => (
                      <motion.div
                        key={fIdx}
                        initial={{ opacity: 0, x: -10 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ type: 'spring', stiffness: 100, damping: 20, delay: fIdx * 0.08 }}
                        className="flex items-start gap-2 text-xs sm:text-sm text-white"
                      >
                        <ShieldCheck className="w-4 h-4 text-brand-yellow-500 shrink-0 mt-0.5" />
                        <span>{feat}</span>
                      </motion.div>
                    ))}
                  </div>
                </div>

                {/* Statistics Row */}
                <motion.div
                  initial={{ opacity: 0, y: 20 }}
                  animate={{ opacity: 1, y: 0 }}
                  transition={{ type: 'spring', stiffness: 100, damping: 20, delay: 0.1 }}
                  className="grid grid-cols-3 gap-3 text-center"
                >
                  <div className="bg-brand-blue-500 border border-brand-blue-500/20 p-3 rounded-xl">
                    <span className="text-xl font-bold font-subheading text-brand-yellow-500 block truncate">
                      {selectedService.stats.time}
                    </span>
                    <span className="text-2xs text-brand-blue-50 font-bold uppercase tracking-wider">Tiempos</span>
                  </div>
                  <div className="bg-brand-blue-500 border border-brand-blue-500/20 p-3 rounded-xl">
                    <span className="text-xl font-bold font-subheading text-white block truncate">
                      {selectedService.stats.price}
                    </span>
                    <span className="text-2xs text-brand-blue-50 font-bold uppercase tracking-wider">Precio Base</span>
                  </div>
                  <div className="bg-brand-blue-500 border border-brand-blue-500/20 p-3 rounded-xl">
                    <span className="text-xl font-bold font-subheading text-brand-yellow-500 block truncate">
                      {selectedService.stats.weight}
                    </span>
                    <span className="text-2xs text-brand-blue-50 font-bold uppercase tracking-wider">Capacidad</span>
                  </div>
                </motion.div>

                {/* Action Footer */}
                <div className="pt-2 flex justify-between items-center gap-4">
                  <motion.button
                    type="button"
                    onClick={() => setSelectedService(null)}
                    whileHover={reduceMotion ? undefined : { x: -4, transition: springConfigSnappy }}
                    whileTap={reduceMotion ? undefined : { scale: 0.98 }}
                    className="text-xs text-brand-blue-50 hover:text-white underline uppercase font-bold tracking-wider cursor-pointer"
                  >
                    Volver Atrás
                  </motion.button>
                  <a
                    href={selectedService.details.ctaHref}
                    className="cta-nested-pill bg-brand-yellow-500 text-brand-blue-500 px-6 py-2.5 text-sm font-subheading font-bold uppercase hover:bg-brand-yellow-400"
                  >
                    <span>{selectedService.details.ctaText}</span>
                    <span className="cta-nested-icon bg-transparent">→</span>
                  </a>
                </div>
              </div>
            </motion.div>
          </motion.div>
        )}
      </AnimatePresence>
    </section>
  );
}

```

### Componente: `src/components/home/EmprendedoresHome.tsx`

```tsx
'use client';

import React from 'react';
import { motion, useReducedMotion, type Variants } from 'motion/react';
import { Building2, ShoppingBag, Landmark, ShieldCheck } from 'lucide-react';
import Link from 'next/link';

export default function EmprendedoresHome() {
  const reduceMotion = useReducedMotion();

  const descriptionText = "Si vendés online, necesitás un socio logístico que responda al toque. Creamos planes a tu medida con tarifas dinámicas transparentes y recolección programada a domicilio en Mar del Plata.";
  const words = descriptionText.split(" ");

  const partners = [
    'TOY PIOLA JUGUETERÍA', 'AMA & POLA', 'DROPIX 3D', 'EL CÓNDOR',
    'STARCEL', 'URBANCOW', 'WANCA', 'CATALINA INDUMENTARIA', 'ENVASES 3G', 'LA PERI'
  ];

  // Spring transition configs
  const springTransition = { type: 'spring' as const, stiffness: 100, damping: 20 };
  const snappySpring = { type: 'spring' as const, stiffness: 300, damping: 25 };

  // Orchestrated section entrance variants
  const sectionVariants: Variants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.12,
        delayChildren: 0.05,
      },
    },
  };

  const itemVariants: Variants = {
    hidden: { opacity: 0, y: 30 },
    visible: {
      opacity: 1,
      y: 0,
      transition: reduceMotion ? { duration: 0.01 } : springTransition,
    },
  };

  const wordContainerVariants: Variants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.03,
        delayChildren: 0.1,
      },
    },
  };

  const wordVariant: Variants = {
    hidden: { opacity: 0, y: 8 },
    visible: {
      opacity: 1,
      y: 0,
      transition: { duration: 0.3, ease: 'easeOut' },
    },
  };

  return (
    <section
      id="emprendedores-home"
      aria-labelledby="emprendedores-home-title"
      className="py-32 md:py-48 bg-brand-blue-500 relative overflow-hidden text-white border-y border-white/10"
    >
      {/* Background Decorative Asymmetric Glows */}
      <div className="absolute top-0 left-0 w-125 h-125 bg-brand-blue-500/5 rounded-full blur-[120px] pointer-events-none" />
      <motion.div
        className="absolute bottom-0 right-0 w-150 h-150 bg-brand-yellow-500/5 rounded-full blur-[150px] pointer-events-none"
        animate={reduceMotion ? {} : { scale: [1, 1.04, 1] }}
        transition={{ duration: 4, ease: 'easeInOut', repeat: Infinity }}
      />

      <motion.div
        className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10"
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, margin: '-50px' }}
        variants={sectionVariants}
      >

        {/* Section Header - Editorial Split with Inline Typography Badge */}
        <motion.div className="max-w-6xl mb-24 space-y-6 text-left" variants={itemVariants}>
          <span className="px-4 py-1.5 bg-brand-blue-50/5 text-brand-yellow-500 border border-brand-yellow-500/20 rounded-full text-xs font-bold tracking-widest inline-block uppercase shadow-sm font-subheading">
            Socio Estratégico Local
          </span>

          <h2 id="emprendedores-home-title" className="text-white text-5xl sm:text-6xl lg:text-7xl font-display uppercase tracking-tight leading-[0.9] text-left max-w-5xl">
            Potenciamos tu{' '}
            <span
              className="inline-flex items-center justify-center w-16 sm:w-20 md:w-24 h-8 sm:h-10 md:h-12 rounded-full align-middle bg-linear-to-r from-brand-yellow-500 to-brand-yellow-400 mx-2 border border-brand-yellow-500 shadow-md text-brand-blue-900 font-display text-base sm:text-xl uppercase transition-transform duration-500 hover:scale-105"
              role="img"
              aria-label="Envíos DosRuedas"
            >
              MDQ
            </span>{' '}
            Marca en Mar del Plata
          </h2>

          <motion.div className="pt-2" variants={wordContainerVariants}>
            <p className="text-brand-blue-50 font-sans text-base sm:text-lg md:text-xl leading-relaxed max-w-3xl font-medium tracking-tight">
              <span className="sr-only">{descriptionText}</span>
              <span aria-hidden="true">
                {words.map((word, i) => (
                  <React.Fragment key={i}>
                    <motion.span
                      variants={wordVariant}
                      className="inline-block"
                    >
                      {word}
                    </motion.span>
                    {i < words.length - 1 ? ' ' : ''}
                  </React.Fragment>
                ))}
              </span>
            </p>
          </motion.div>

          <div className="h-0.5 w-24 bg-brand-yellow-500 rounded-full pt-1" />
        </motion.div>

        {/* Solutions Cards Grid: Asymmetric Bento Layout with Double-Bezel Cards */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8 auto-rows-auto lg:auto-rows-85 grid-flow-row-dense">
          
          {/* Card 1: PyMEs (E-Commerce) - lg:col-span-7 lg:row-span-2 (Dark Navy Card with Double-Layered Glass Shell) */}
          <motion.div
            variants={itemVariants}
            className="lg:col-span-7 lg:row-span-2 p-3 sm:p-4 rounded-[30px] bg-white/10 backdrop-blur-md border border-white/20 hover:border-brand-yellow-400/40 hover:shadow-glow-yellow transition-all duration-300 group overflow-hidden flex flex-col"
            whileHover={reduceMotion ? undefined : { y: -6, transition: snappySpring }}
          >
            <div className="rounded-[20px] bg-brand-blue p-6 sm:p-8 border border-white/10 flex flex-col justify-between h-full relative overflow-hidden text-left flex-1">
              {/* Subtle Radial Glow */}
              <motion.div
                className="absolute bottom-0 right-0 w-48 h-48 rounded-full bg-brand-yellow-500/10 blur-3xl pointer-events-none"
                animate={reduceMotion ? {} : { scale: [1, 1.08, 1], opacity: [0.08, 0.16, 0.08] }}
                transition={{ duration: 3, ease: 'easeInOut', repeat: Infinity }}
              />

              {/* Watermark Background Icon */}
              <motion.div
                className="absolute right-4 bottom-4 text-white opacity-[0.03] pointer-events-none select-none"
                animate={reduceMotion ? {} : { rotate: [0, 2, -2, 0], scale: [1, 1.03, 1] }}
                transition={{ duration: 5, ease: 'easeInOut', repeat: Infinity }}
              >
                <Landmark className="w-44 h-44" />
              </motion.div>

              <div className="space-y-6 relative z-10">
                <div className="flex justify-between items-start">
                  <motion.div
                    className="p-3 bg-brand-yellow-500 text-brand-blue-500 rounded-xl shadow-[2px_2px_0px_var(--color-brand-blue-500)]"
                    whileHover={reduceMotion ? undefined : { scale: 1.08, transition: snappySpring }}
                  >
                    <Landmark className="h-5 w-5" />
                  </motion.div>
                  <span className="text-2xs font-bold tracking-widest bg-brand-blue-500 text-brand-yellow-500 px-3 py-1.5 rounded-lg uppercase font-subheading border border-brand-yellow-500/30">
                    EMPRENDEDORES
                  </span>
                </div>

                <div className="space-y-2">
                  <motion.h3
                    className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-white group-hover:text-brand-yellow-500 transition-colors"
                    whileHover={reduceMotion ? undefined : { x: 4, transition: snappySpring }}
                  >
                    Cuenta Corriente Flexible
                  </motion.h3>
                  <p className="text-brand-blue-50 text-sm leading-relaxed font-sans">
                    Tu equipo de entregas de confianza, aunque la cantidad de pedidos cambie cada
                    día. Pagás los envíos juntos, por semana, quincena o mes.
                  </p>
                </div>

                <ul className="space-y-2.5 pt-2">
                  {[
                    'Sin volumen mínimo de envíos: entrás con la cantidad que tengas',
                    'Accedés a tarifas LowCost con franjas horarias de 3 hs, como Express',
                    'Trabajás de forma exclusiva con nosotros para tus envíos',
                    'Entregas contrareembolso integradas sin cargo extra',
                  ].map((feat) => (
                    <li
                      key={feat}
                      className="flex items-start gap-2 text-xs sm:text-sm text-white font-sans"
                    >
                      <ShieldCheck className="h-4.5 w-4.5 text-brand-yellow-500 shrink-0 mt-0.5" />
                      <span>{feat}</span>
                    </li>
                  ))}
                </ul>
              </div>

              <div className="pt-6 mt-6 border-t border-white/10 relative z-10 flex justify-end">
                <Link
                  href="/servicios/empresas-cuenta-corriente"
                  className="inline-flex items-center justify-between rounded-full min-h-13 px-8 py-3.5 bg-brand-yellow-400 hover:bg-brand-yellow-300 text-brand-blue-500 font-subheading text-base font-bold uppercase tracking-wider shadow-glow-yellow transition-all duration-300 hover:scale-[1.02] cursor-pointer group"
                >
                  <span>Conocé más</span>
                  <span className="inline-flex items-center justify-center w-8 h-8 rounded-full bg-transparent text-brand-blue ml-3 transition-transform duration-300 group-hover:translate-x-1">
                    →
                  </span>
                </Link>
              </div>
            </div>
          </motion.div>

          {/* Card 2: MercadoLibre Flex - lg:col-span-5 lg:row-span-1 (Yellow Card) */}
          <motion.div
            variants={itemVariants}
            className="lg:col-span-5 lg:row-span-1 double-bezel-outer p-2 rounded-2xl bg-brand-yellow-500/10 border border-brand-yellow-500/20 hover:border-brand-blue-700/30 hover:bg-brand-yellow-500/15 hover:shadow-[0_20px_40px_-15px_rgba(255,236,1,0.15)] group overflow-hidden flex flex-col"
            whileHover={reduceMotion ? undefined : { y: -6, transition: snappySpring }}
          >
            <div className="double-bezel-inner bg-linear-to-br from-brand-yellow-500 to-brand-yellow-400 p-6 sm:p-8 rounded-xl border border-brand-yellow-500/20 shadow-sm flex flex-col justify-between h-full relative overflow-hidden text-left text-brand-blue-900 flex-1">
              {/* Subtle Radial Glow */}
              <motion.div
                className="absolute bottom-0 right-0 w-36 h-36 rounded-full bg-white/20 blur-2xl pointer-events-none"
                animate={reduceMotion ? {} : { scale: [1, 1.08, 1], opacity: [0.15, 0.25, 0.15] }}
                transition={{ duration: 3, ease: 'easeInOut', repeat: Infinity }}
              />

              {/* Watermark Background Icon */}
              <motion.div
                className="absolute right-4 bottom-4 text-brand-blue-900 opacity-[0.04] pointer-events-none select-none"
                animate={reduceMotion ? {} : { rotate: [0, -2, 2, 0], scale: [1, 1.03, 1] }}
                transition={{ duration: 5, ease: 'easeInOut', repeat: Infinity }}
              >
                <ShoppingBag className="w-32 h-32" />
              </motion.div>

              <div className="space-y-4 relative z-10">
                <div className="flex justify-between items-start">
                  <motion.div
                    className="p-3 bg-brand-blue-500 text-white rounded-xl shadow-[2px_2px_0px_var(--color-brand-blue-500)]"
                    whileHover={reduceMotion ? undefined : { scale: 1.08, transition: snappySpring }}
                  >
                    <ShoppingBag className="h-5 w-5" />
                  </motion.div>
                  <span className="text-2xs font-bold tracking-widest bg-brand-blue-500 text-white px-3 py-1.5 rounded-lg uppercase font-subheading border border-brand-blue-500/30">
                    MERCADOLIBRE
                  </span>
                </div>

                <div className="space-y-1">
                  <h3 className="text-xl sm:text-2xl font-display uppercase tracking-tight text-brand-blue-500">
                    Envíos Flex Meli
                  </h3>
                  <p className="text-brand-blue-500 text-xs sm:text-sm leading-relaxed font-sans font-medium">
                    Servicio adaptado a los estándares de Mercado Envíos Flex para tus envíos rápidos en el día. Recolección en tu local y entrega puntual garantizada.
                  </p>
                </div>
              </div>

              <div className="pt-4 mt-4 border-t border-brand-blue-100 relative z-10 flex justify-end">
                <Link
                  href="/servicios/enviosflex"
                  className="cta-nested-pill bg-brand-blue-500 text-white px-6 py-2.5 text-xs font-bold tracking-wider font-subheading rounded-full flex items-center gap-2 shadow-md hover:bg-brand-blue-400"
                >
                  <span>Configurar Flex</span>
                  <span className="cta-nested-icon bg-white/10 w-6 h-6 rounded-full flex items-center justify-center">
                    →
                  </span>
                </Link>
              </div>
            </div>
          </motion.div>

          {/* Card 3: Corporativos (White Card) - lg:col-span-5 lg:row-span-1 */}
          <motion.div
            variants={itemVariants}
            className="lg:col-span-5 lg:row-span-1 double-bezel-outer p-2 rounded-2xl bg-brand-blue-50/80 border border-brand-blue-100 hover:border-brand-blue-300 hover:shadow-antigravity-deep group overflow-hidden flex flex-col"
            whileHover={reduceMotion ? undefined : { y: -6, transition: snappySpring }}
          >
            <div className="double-bezel-inner bg-white p-6 sm:p-8 rounded-xl border border-brand-blue-50/50 shadow-sm flex flex-col justify-between h-full relative overflow-hidden text-left text-brand-ink flex-1">
              {/* Subtle Radial Glow */}
              <motion.div
                className="absolute bottom-0 right-0 w-36 h-36 rounded-full bg-brand-blue-500/5 blur-2xl pointer-events-none"
                animate={reduceMotion ? {} : { scale: [1, 1.08, 1], opacity: [0.08, 0.16, 0.08] }}
                transition={{ duration: 3, ease: 'easeInOut', repeat: Infinity }}
              />

              {/* Watermark Background Icon */}
              <motion.div
                className="absolute right-4 bottom-4 text-brand-blue-700 opacity-[0.02] pointer-events-none select-none"
                animate={reduceMotion ? {} : { rotate: [0, 2, -2, 0], scale: [1, 1.03, 1] }}
                transition={{ duration: 5, ease: 'easeInOut', repeat: Infinity }}
              >
                <Building2 className="w-32 h-32" />
              </motion.div>

              <div className="space-y-4 relative z-10">
                <div className="flex justify-between items-start">
                  <motion.div
                    className="p-3 bg-brand-yellow-500 text-brand-blue-500 rounded-xl shadow-[2px_2px_0px_var(--color-brand-blue-500)]"
                    whileHover={reduceMotion ? undefined : { scale: 1.08, transition: snappySpring }}
                  >
                    <Building2 className="h-5 w-5" />
                  </motion.div>
                  <span className="text-2xs font-bold tracking-widest bg-brand-blue-50 text-brand-blue-500 px-3 py-1.5 rounded-lg uppercase font-subheading border border-brand-blue-100">
                    CORPORATIVO
                  </span>
                </div>

                <div className="space-y-1">
                  <h3 className="text-xl sm:text-2xl font-display uppercase tracking-tight text-brand-blue-500 group-hover:text-brand-blue-400 transition-colors">
                    Soluciones Corporativas
                  </h3>
                  <p className="text-brand-blue-500 text-xs sm:text-sm leading-relaxed font-sans">
                    Soporte a gran escala con pagos agrupados (semanales, quincenales o mensuales), ruteos
                    especiales para grandes volúmenes y entregas express coordinadas en Mar del Plata.
                  </p>
                </div>
              </div>

              <div className="pt-4 mt-4 border-t border-brand-blue-100 relative z-10 flex justify-end">
                <Link
                  href="/contacto"
                  className="cta-nested-pill bg-brand-yellow-500 text-brand-blue-500 px-6 py-2.5 text-xs font-bold tracking-wider font-subheading rounded-full flex items-center gap-2 shadow-sm hover:bg-brand-yellow-400"
                >
                  <span>Abrir Cuenta Corriente</span>
                  <span className="cta-nested-icon bg-transparent w-6 h-6 rounded-full flex items-center justify-center">
                    →
                  </span>
                </Link>
              </div>
            </div>
          </motion.div>

        </div>

        {/* Marquee of Local Partners - GPU Hardware Accelerated Infinite Scroll */}
        <motion.div
          variants={itemVariants}
          className="mt-24 pt-12 border-t border-brand-blue-500/10"
        >
          <p className="text-center font-subheading text-xs tracking-widest text-brand-blue-50 mb-6 uppercase">
            Marcas locales que confían en nosotros
          </p>
          <div
            className="relative w-full overflow-hidden py-4 select-none mask-[linear-gradient(to_right,transparent,black_10%,black_90%,transparent)]"
          >
            <div className="flex gap-16 w-max animate-logos-scroll hover:[animation-play-state:paused] focus-within:[animation-play-state:paused]">
              {/* Set 1 */}
              <div className="flex gap-16 items-center">
                {partners.map((partner, index) => (
                  <span
                    key={index}
                    className="font-display text-2xl tracking-wider text-brand-blue-50 uppercase cursor-default hover:text-brand-yellow-500 hover:scale-105 transition-all duration-300"
                  >
                    {partner}
                  </span>
                ))}
              </div>
              {/* Set 2 (for infinite continuous loop) */}
              <div className="flex gap-16 items-center" aria-hidden="true">
                {partners.map((partner, index) => (
                  <span
                    key={`dup-${index}`}
                    className="font-display text-2xl tracking-wider text-brand-blue-50 uppercase cursor-default hover:text-brand-yellow-500 hover:scale-105 transition-all duration-300"
                  >
                    {partner}
                  </span>
                ))}
              </div>
            </div>
          </div>
        </motion.div>

      </motion.div>
    </section>
  );
}

```

### Componente: `src/components/home/CtaSection.tsx`

```tsx
'use client';

import React, { useState } from 'react';
import { motion, useReducedMotion, type Variants } from 'motion/react';
import { MessageSquare, User, Store, PackageSearch } from 'lucide-react';

export default function CtaSection() {
  const reduceMotion = useReducedMotion();
  const [formData, setFormData] = useState({ name: '', business: '', volume: '' });

  const handleWhatsAppRedirect = (e: React.FormEvent) => {
    e.preventDefault();
    const { name, business, volume } = formData;
    const message = `Hola, soy ${name} de ${business}. Me interesa cotizar envíos para ${volume} paquetes mensuales.`;
    const encodedMessage = encodeURIComponent(message);
    window.open(`https://wa.me/5492236602699?text=${encodedMessage}`, '_blank');
  };

  // HyperFrames standard spring config
  const springConfig = { type: 'spring' as const, stiffness: 100, damping: 20 };
  const springConfigSnappy = { type: 'spring' as const, stiffness: 300, damping: 25 };

  // Container variants with orchestrated stagger
  const containerVariants: Variants = {
    hidden: { opacity: 0 },
    visible: {
      opacity: 1,
      transition: {
        staggerChildren: 0.1,
        delayChildren: 0.05,
      },
    },
  };

  const itemVariants: Variants = {
    hidden: { opacity: 0, y: 24 },
    visible: {
      opacity: 1,
      y: 0,
      transition: reduceMotion ? { duration: 0.01 } : springConfig,
    },
  };

  return (
    <section
      id="cta-section"
      aria-labelledby="cta-section-title"
      className="py-20 lg:py-28 bg-brand-blue-500 relative z-10 overflow-hidden px-4 sm:px-6 lg:px-8 shadow-2xl"
    >
      <motion.div
        className="max-w-6xl mx-auto p-2.5 sm:p-3.5 rounded-[30px] bg-white/10 backdrop-blur-md border border-white/25 shadow-2xl"
        initial="hidden"
        whileInView="visible"
        viewport={{ once: true, margin: '-50px' }}
        variants={containerVariants}
      >
        <motion.div
          className="bg-white rounded-[20px] p-8 sm:p-12 lg:p-14 flex flex-col lg:flex-row items-center gap-10 lg:gap-16 border border-brand-blue-100/50 shadow-sm relative overflow-hidden"
          variants={itemVariants}
        >

          {/* Background grid */}
          <div className="absolute inset-0 bg-[linear-gradient(to_right,rgba(9,80,246,0.03)_1px,transparent_1px),linear-gradient(to_bottom,rgba(9,80,246,0.03)_1px,transparent_1px)] bg-size-[24px_24px] pointer-events-none" />

          {/* Left Text Block */}
          <motion.div className="lg:w-1/2 space-y-8 relative z-10 text-center lg:text-left" variants={itemVariants}>
            <motion.div
              className="inline-flex"
              whileHover={reduceMotion ? undefined : { scale: 1.03, transition: springConfigSnappy }}
            >
              <span className="px-4 py-2 rounded-full text-xs font-subheading tracking-widest bg-brand-yellow-400/20 text-brand-blue-500 border border-brand-yellow-400 uppercase font-bold cursor-default shadow-glow-yellow">
                Cotización Inmediata
              </span>
            </motion.div>

            <motion.h2 id="cta-section-title" className="text-brand-blue-500 font-display text-4xl sm:text-5xl lg:text-6xl uppercase leading-[0.98] tracking-tight">
              ¿Listo para escalar la logística de tu e-commerce?
            </motion.h2>

            <motion.p className="text-brand-blue-500 text-base sm:text-lg font-sans leading-relaxed font-medium">
              Olvidate de la gestión de paquetes en Mar del Plata. Completá tus datos y te respondemos por WhatsApp al instante.
            </motion.p>

            <motion.div
              className="pt-2 hidden lg:block cursor-default"
              whileHover={reduceMotion ? undefined : { x: 4, transition: springConfigSnappy }}
            >
              <p className="text-xs font-mono tracking-widest text-brand-blue-500 font-bold uppercase leading-none">
                Atención comercial <span className="text-brand-yellow-400 bg-brand-blue-500 px-2 py-0.5 rounded font-mono">{'<'} 5 MIN</span>
              </p>
            </motion.div>
          </motion.div>

          {/* Right Form Block */}
          <motion.div className="lg:w-1/2 w-full relative z-10" variants={itemVariants}>
            <form onSubmit={handleWhatsAppRedirect} className="space-y-5 bg-brand-blue-50 p-6 sm:p-8 rounded-[20px] border-2 border-brand-blue-100/20 shadow-xl">

              <motion.div
                className="space-y-1.5"
                whileHover={reduceMotion ? undefined : { x: 3, transition: springConfigSnappy }}
              >
                <label htmlFor="cta-name" className="text-xs font-subheading tracking-wider text-brand-blue-500 uppercase font-bold">Tu Nombre</label>
                <div className="relative">
                  <div className="absolute left-3.5 top-1/2 -translate-y-1/2 h-5 w-5 text-brand-blue-500/60 pointer-events-none">
                    <User className="w-5 h-5" />
                  </div>
                  <input
                    id="cta-name"
                    name="nombre"
                    autoComplete="name"
                    required
                    value={formData.name}
                    onChange={e => setFormData({...formData, name: e.target.value})}
                    type="text"
                    placeholder="Ingresá tu nombre"
                    className="w-full h-11 border-2 border-brand-blue-100/20 rounded-xl pl-11 pr-4 focus:outline-none focus:border-brand-blue-500 focus:ring-2 focus:ring-brand-blue-500/20 text-brand-blue-500 placeholder:text-brand-blue-500/40 text-sm font-sans transition-colors bg-white"
                  />
                </div>
              </motion.div>

              <motion.div
                className="space-y-1.5"
                whileHover={reduceMotion ? undefined : { x: 3, transition: springConfigSnappy }}
              >
                <label htmlFor="cta-business" className="text-xs font-subheading tracking-wider text-brand-blue-500 uppercase font-bold">Empresa / Negocio</label>
                <div className="relative">
                  <div className="absolute left-3.5 top-1/2 -translate-y-1/2 h-5 w-5 text-brand-blue-500/60 pointer-events-none">
                    <Store className="w-5 h-5" />
                  </div>
                  <input
                    id="cta-business"
                    name="empresa"
                    autoComplete="organization"
                    required
                    value={formData.business}
                    onChange={e => setFormData({...formData, business: e.target.value})}
                    type="text"
                    placeholder="Nombre de tu emprendimiento"
                    className="w-full h-11 border-2 border-brand-blue-100/20 rounded-xl pl-11 pr-4 focus:outline-none focus:border-brand-blue-500 focus:ring-2 focus:ring-brand-blue-500/20 text-brand-blue-500 placeholder:text-brand-blue-500/40 text-sm font-sans transition-colors bg-white"
                  />
                </div>
              </motion.div>

              <motion.div
                className="space-y-1.5"
                whileHover={reduceMotion ? undefined : { x: 3, transition: springConfigSnappy }}
              >
                <label htmlFor="volume-select" className="text-xs font-subheading tracking-wider text-brand-blue-500 uppercase font-bold">Volumen Estimado Mensual</label>
                <div className="relative">
                  <div className="absolute left-3.5 top-1/2 -translate-y-1/2 h-5 w-5 text-brand-blue-500/60 pointer-events-none">
                    <PackageSearch className="w-5 h-5" />
                  </div>
                  <select
                    required
                    id="volume-select"
                    name="volumen"
                    value={formData.volume}
                    onChange={e => setFormData({...formData, volume: e.target.value})}
                    className="w-full h-11 border-2 border-brand-blue-100/20 rounded-xl pl-11 pr-4 focus:outline-none focus:border-brand-blue-500 focus:ring-2 focus:ring-brand-blue-500/20 text-brand-blue-500 text-sm font-sans transition-colors appearance-none bg-white cursor-pointer"
                  >
                    <option value="" disabled>Seleccioná una opción</option>
                    <option value="1 a 50">1 a 50 envíos</option>
                    <option value="51 a 200">51 a 200 envíos</option>
                    <option value="Más de 200">Más de 200 envíos</option>
                  </select>
                </div>
              </motion.div>

              <motion.div className="pt-4">
                <motion.button
                  type="submit"
                  whileHover={
                    reduceMotion
                      ? undefined
                      : { scale: 1.02, transition: springConfigSnappy }
                  }
                  whileTap={reduceMotion ? undefined : { scale: 0.98, transition: springConfigSnappy }}
                  className="w-full min-h-13 bg-brand-yellow-400 hover:bg-brand-yellow-300 text-brand-blue-500 font-subheading tracking-wider text-xl uppercase rounded-full shadow-glow-yellow flex items-center justify-center gap-3 cursor-pointer font-bold transition-all"
                >
                  <span>Hablar por WhatsApp</span>
                  <motion.span
                    className="h-5 w-5"
                    whileHover={reduceMotion ? undefined : { scale: 1.15, rotate: 10, transition: springConfigSnappy }}
                  >
                    <MessageSquare className="w-5 h-5" />
                  </motion.span>
                </motion.button>
              </motion.div>

            </form>
          </motion.div>

        </motion.div>
      </motion.div>
    </section>
  );
}
```

### Componente: `src/components/home/SocialProofSection.tsx`

```tsx
'use client';

import React from 'react';
import Link from 'next/link';
import { Star, ExternalLink } from 'lucide-react';
import { cn } from '@/lib/utils';

interface Review {
  id: string;
  author: string;
  timeAgo: string;
  quoteHighlight: string;
  text: string;
  // color variant: 'blue' | 'white' | 'yellow'
  variant: 'blue' | 'white' | 'yellow';
}

// 6 reviews selected from source data, cleaned of emojis, no ownerResponse
const REVIEWS: Review[] = [
  {
    id: 'karen-herrera',
    author: 'Karen Herrera',
    timeAgo: 'Hace 13 semanas',
    quoteHighlight: 'RESOLVIERON MI PROBLEMA CON LA MEJOR PREDISPOSICIÓN',
    text: 'Excelente el servicio, rápidos, muy atentos, resolvieron mi problema con la mejor predisposición, los recomiendo ampliamente.',
    variant: 'blue',
  },
  {
    id: 'agustin-torres',
    author: 'Agustin Torres',
    timeAgo: 'Hace 48 semanas',
    quoteHighlight: 'IMPECABLE PARA LLEVAR PEDIDOS A NUESTROS CLIENTES',
    text: 'Lo usé varias veces para llevar pedidos a nuestros clientes. Impecable el servicio. Además hacen depósitos en cajeros sin problemas. Unos genios.',
    variant: 'white',
  },
  {
    id: 'alexis-bogarin',
    author: 'Alexis Bogarin',
    timeAgo: 'Hace 37 semanas',
    quoteHighlight: 'EL MEJOR SERVICIO PREMIUM DE LA ZONA',
    text: 'El mejor servicio premium de la zona en Mar del Plata. 100% recomendable por puntualidad y trato.',
    variant: 'yellow',
  },
  {
    id: 'lorenzo-elizagoyen',
    author: 'Lorenzo Elizagoyen',
    timeAgo: 'Hace 32 semanas',
    quoteHighlight: 'ATENCIÓN DE PRIMERA, RÁPIDO, CONFIABLE Y SEGURO',
    text: 'Excelente servicio, atención de primera, rápido, confiable y seguro. Recomendado 100% para envíos puntuales.',
    variant: 'white',
  },
  {
    id: 'emiliano-garri',
    author: 'Emiliano Garri',
    timeAgo: 'Hace 48 semanas',
    quoteHighlight: '¡LA MEJOR MENSAJERÍA DE MDP!',
    text: 'La mejor mensajería de Mar del Plata. Cumplen siempre con lo prometido y no te dejan tirado.',
    variant: 'blue',
  },
  {
    id: 'nahuari',
    author: 'NahuAri',
    timeAgo: 'Hace 48 semanas',
    quoteHighlight: '10 DE 10, RESPONSABLES POR SOBRE TODAS LAS COSAS',
    text: '10 de 10 muy buenos en lo que hacen, responsables por sobre todas las cosas, super recomendable para tu negocio.',
    variant: 'white',
  },
];

function ReviewCard({ review }: { review: Review }) {
  const stars = (
    <div aria-label="Calificación: 5 de 5 estrellas" className="flex gap-1" role="img">
      <span className="text-xl">★</span>
      <span className="text-xl">★</span>
      <span className="text-xl">★</span>
      <span className="text-xl">★</span>
      <span className="text-xl">★</span>
    </div>
  );

  const cardStyles = {
    blue: {
      article: 'bg-brand-blue-500 text-white shadow-elevated',
      dateBadge: 'bg-brand-yellow-500 text-brand-blue-500',
      starsColor: 'text-brand-yellow-500',
      headingColor: 'text-white',
      bodyColor: 'text-white/90',
      borderColor: 'border-white/20',
      avatarBg: 'bg-brand-yellow-500 text-brand-blue-500',
      authorColor: 'text-white',
    },
    white: {
      article: 'bg-white border-2 border-brand-yellow-500 shadow-[0_16px_40px_rgba(9,80,246,0.08)]',
      dateBadge: 'bg-brand-blue-50 text-brand-blue-500',
      starsColor: 'text-brand-blue-500',
      headingColor: 'text-brand-blue-500',
      bodyColor: 'text-brand-blue-500/85',
      borderColor: 'border-brand-blue-100/40',
      avatarBg: 'bg-brand-blue-500 text-white',
      authorColor: 'text-brand-blue-500',
    },
    yellow: {
      article: 'bg-brand-yellow-500 text-brand-blue-500 shadow-[0_16px_40px_rgba(255,236,1,0.3)]',
      dateBadge: 'bg-white text-brand-blue-500 shadow-sm',
      starsColor: 'text-brand-blue-500',
      headingColor: 'text-brand-blue-500',
      bodyColor: 'text-brand-blue-500',
      borderColor: 'border-brand-blue-500/20',
      avatarBg: 'bg-brand-blue-500 text-white',
      authorColor: 'text-brand-blue-500',
    },
  }[review.variant];

  return (
    <article className={cn(
      'card-token flex flex-col justify-between p-8 min-h-85',
      cardStyles.article
    )}>
      <div>
        {/* Top Row: Rating & Date */}
        <div className="flex items-center justify-between mb-6">
          <div aria-label="Calificación: 5 de 5 estrellas" className={cn('flex gap-1', cardStyles.starsColor)}>
            {stars}
          </div>
          <span className={cn(
            'text-xs font-bold px-3.5 py-1 rounded-full font-mono',
            cardStyles.dateBadge
          )}>
            {review.timeAgo}
          </span>
        </div>

        {/* Review Heading */}
        <h3 className={cn(
          'font-subheading text-xl lg:text-2xl uppercase leading-none mb-3 tracking-wide',
          cardStyles.headingColor
        )}>
          {review.quoteHighlight}
        </h3>

        {/* Review Body */}
        <p className={cn('text-sm leading-relaxed font-normal', cardStyles.bodyColor)}>
          {review.text}
        </p>
      </div>

      {/* Author / Footer */}
      <div className={cn('pt-6 mt-6 flex items-center gap-3', cardStyles.borderColor)}>
        <div className={cn(
          'w-10 h-10 rounded-full font-bold flex items-center justify-center text-sm shrink-0 shadow-sm',
          cardStyles.avatarBg
        )}>
          {review.author.charAt(0)}
        </div>
        <span className={cn('font-bold text-sm tracking-wide', cardStyles.authorColor)}>
          {review.author}
        </span>
      </div>
    </article>
  );
}

export default function SocialProofSection() {
  return (
    <section
      id="social-proof"
      aria-labelledby="social-proof-title"
      className="relative py-24 bg-brand-blue-50 border-y border-brand-blue-100/60"
    >
      <div className="mx-auto max-w-[80rem] px-6 lg:px-8">
        {/* Header */}
        <header className="mb-10 lg:mb-14">
          {/* Rating Trust Badge */}
          <div className="inline-flex items-center mb-5">
            <span className="inline-flex items-center gap-1.5 bg-brand-blue-500 text-white text-[12px] sm:text-[13px] font-mono font-bold px-5 py-2 rounded-full tracking-wider uppercase shadow-md">
              5.0 / 5.0 EN GOOGLE · +120 VALORACIONES
            </span>
          </div>

          {/* Main Title & CTA Button */}
          <div className="flex flex-col lg:flex-row lg:items-end justify-between gap-6">
            {/* Title with highlighted keyword */}
            <h1
              id="social-proof-title"
              className="font-display uppercase text-brand-blue-500 text-[42px] sm:text-[60px] lg:text-[clamp(2.75rem,5.2vw,4.5rem)] leading-[0.92] max-w-4xl tracking-tight"
            >
              LA PALABRA DE QUIENES
              <span className="inline-block relative mx-1 my-1 px-4 sm:px-5 py-1 rounded-full bg-brand-yellow-500 text-brand-blue-500 shadow-cta-glow">
                VENDEN Y ENVÍAN
              </span>
              EN MDQ
            </h1>

            {/* Google Maps Link Button */}
            <div className="shrink-0 pt-2 lg:pt-0">
              <Link
                href="https://share.google/ofw5wAQt3Fc1dArom"
                target="_blank"
                rel="noopener noreferrer"
                className="button-pill inline-flex items-center gap-2.5 border-2 border-brand-blue-500 text-brand-blue-500 hover:bg-brand-blue-500 hover:text-white px-7 py-3 font-subheading text-lg sm:text-xl tracking-wider uppercase shadow-sm hover:shadow-md"
                aria-label="Ver todas las opiniones en Google Maps"
              >
                <span>VER EN GOOGLE MAPS</span>
                <ExternalLink className="w-4 h-4 stroke-[2.5]" fill="none" stroke="currentColor" viewBox="0 0 24 24" aria-hidden="true">
                  <path d="M4.5 19.5l15-15m0 0H8.25m11.25 0v11.25" strokeLinecap="round" strokeLinejoin="round" />
                </ExternalLink>
              </Link>
            </div>
          </div>
        </header>

        {/* Testimonials Grid: 3×2 = 6 cards */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {REVIEWS.map((review) => (
            <ReviewCard key={review.id} review={review} />
          ))}
        </div>
      </div>
    </section>
  );
}
```

---

## 3. Estructura de Layout Compartido y Estilos Globales

### Global CSS Styles & Design Tokens (`src/app/globals.css`)

```css
@import "tailwindcss";

/* Tailwind CSS v4 Custom Variant */
@custom-variant dark (&:where(.dark, .dark *));

:root {
  /* ========================================================================
   * SUPERFICIES Y ACCIONES (fuera de @theme para no chocar con text-* font-size)
   * ======================================================================== */
  --surface-page: var(--color-white);
  --surface-card: var(--color-white);
  --surface-muted: var(--color-brand-blue-50);
  --surface-invert: var(--color-brand-blue-700);
  --surface-glass: rgba(255, 255, 255, 0.06);
  --text-body: var(--color-brand-blue-900);
  --text-muted: var(--color-brand-blue-400);
  --text-heading: var(--color-brand-blue-900);
  --text-on-invert: var(--color-white);
  --text-on-accent: var(--color-brand-blue-900);
  --border-subtle: var(--color-brand-blue-100);
  --focus-ring: var(--color-brand-blue-500);
  --action-primary: var(--color-brand-blue-700);
  --action-primary-hover: var(--color-brand-blue-800);
  --action-accent: var(--color-brand-yellow-500);
  --action-accent-hover: var(--color-brand-yellow-400);
  --action-danger: #EF4444;
}

@theme {
  /* ========================================================================
   * PALETA CANÓNICA — Ley de Tres Colores (Ajuste Max #0950F6)
   * Cada token tiene un hex literal. Nada más oscuro que #0950F6.
   * ======================================================================== */

  /* Azul Vibrante — 6 pasos (50 → 500). 500/600/700/900/950 colapsan a #0950F6. */
  --color-brand-blue-50: #E6EEFE;   /* fondo suave, bezel exterior /80, skeleton, hover ghost */
  --color-brand-blue-100: #BACEFD;  /* borde estructural, divisores, stepper línea pendiente */
  --color-brand-blue-200: #8EAFFB;  /* hover borde tarjeta, anillo radio pendiente, trazos SVG */
  --color-brand-blue-300: #628FF9;  /* borde input reposo, hover bezel, trazos SVG secundarios */
  --color-brand-blue-400: #3570F8;  /* íconos, texto grande muted (≥24px). Falla AA en texto normal */
  --color-brand-blue-500: #0950F6;  /* anillo de foco, primario canónico */

  /* Colapsados al tope #0950F6 — el nombre elige la FUNCIÓN, no la oscuridad */
  --color-brand-blue-600: #0950F6;  /* colapsado al tope */
  --color-brand-blue-700: #0950F6;  /* PRIMARIO: lienzo institucional, header, footer, hero, H1/H2 */
  --color-brand-blue-800: #3570F8;  /* hover de FONDOS azules (se aclara porque no se puede oscurecer) */
  --color-brand-blue-900: #0950F6;  /* texto sobre amarillo y cuerpo en tarjetas (4.9:1) */
  --color-brand-blue-950: #0950F6;  /* colapsado al tope (footer profundo = mismo azul) */

  /* Amarillo Vial — 7 pasos (50 → 600). Señal, nunca superficie. ≤15% cobertura. */
  --color-brand-yellow-50: #FFFDE6;  /* fondo Flex seleccionado */
  --color-brand-yellow-100: #FFFAB8; /* badge flex, anillo step completado, halos */
  --color-brand-yellow-200: #FFF78A; /* borde Flex seleccionado */
  --color-brand-yellow-300: #FFF45C; /* detalle mono sobre azul */
  --color-brand-yellow-400: #FFF12E; /* hover CTA primario y WhatsApp */
  --color-brand-yellow-500: #FFEC01; /* CTA primario, step completado/activo, precio sobre azul, franja footer 6px */
  --color-brand-yellow-600: #E6D400; /* pressed del CTA */

  /* Blanco — lienzo único */
  --color-white: #FFFFFF;

  /* ========================================================================
   * ALIAS SEMÁNTICOS CANÓNICOS (referencian a la paleta de arriba)
   * ======================================================================== */
  --color-brand-blue: var(--color-brand-blue-700);
  --color-brand-yellow: var(--color-brand-yellow-500);
  --color-brand-ink: var(--color-brand-blue-900);
  --color-brand-white: var(--color-white);

  /* ========================================================================
   * REDES DE SEGURIDAD: escalas remapeadas a marca (no son API válida)
   * Código nuevo usa solo brand-*. Estas evitan que clases heredadas rompan.
   * ======================================================================== */
  --color-blue-50: var(--color-brand-blue-50);
  --color-blue-100: var(--color-brand-blue-100);
  --color-blue-200: var(--color-brand-blue-200);
  --color-blue-300: var(--color-brand-blue-300);
  --color-blue-400: var(--color-brand-blue-400);
  --color-blue-500: var(--color-brand-blue-500);
  --color-blue-600: var(--color-brand-blue-500);
  --color-blue-700: var(--color-brand-blue-700);
  --color-blue-800: var(--color-brand-blue-400);
  --color-blue-900: var(--color-brand-blue-700);
  --color-blue-950: var(--color-brand-blue-700);

  --color-gray-50: var(--color-white);
  --color-gray-100: var(--color-brand-blue-50);
  --color-gray-200: var(--color-brand-blue-100);
  --color-gray-300: var(--color-brand-blue-200);
  --color-gray-400: var(--color-brand-blue-300);
  --color-gray-500: var(--color-brand-blue-400);
  --color-gray-600: var(--color-brand-blue-500);
  --color-gray-700: var(--color-brand-blue-700);
  --color-gray-800: var(--color-brand-blue-700);
  --color-gray-900: var(--color-brand-blue-700);
  --color-gray-950: var(--color-brand-blue-700);

  --color-slate-50: var(--color-white);
  --color-slate-100: var(--color-brand-blue-50);
  --color-slate-200: var(--color-brand-blue-100);
  --color-slate-300: var(--color-brand-blue-200);
  --color-slate-400: var(--color-brand-blue-300);
  --color-slate-500: var(--color-brand-blue-400);
  --color-slate-600: var(--color-brand-blue-500);
  --color-slate-700: var(--color-brand-blue-700);
  --color-slate-800: var(--color-brand-blue-700);
  --color-slate-900: var(--color-brand-blue-700);
  --color-slate-950: var(--color-brand-blue-700);

  --color-zinc-50: var(--color-white);
  --color-zinc-100: var(--color-brand-blue-50);
  --color-zinc-200: var(--color-brand-blue-100);
  --color-zinc-300: var(--color-brand-blue-200);
  --color-zinc-400: var(--color-brand-blue-300);
  --color-zinc-500: var(--color-brand-blue-400);
  --color-zinc-600: var(--color-brand-blue-500);
  --color-zinc-700: var(--color-brand-blue-700);
  --color-zinc-800: var(--color-brand-blue-700);
  --color-zinc-900: var(--color-brand-blue-700);
  --color-zinc-950: var(--color-brand-blue-700);

  /* ========================================================================
   * NEUTRALIZACIÓN DE PALETAS PROHIBIDAS (Tailwind defaults)
   * Se ponen a `initial` para que no generen CSS. Confirmado: 0 usos en src/.
   * ======================================================================== */
  --color-neutral-50: initial; --color-neutral-100: initial; --color-neutral-200: initial;
  --color-neutral-300: initial; --color-neutral-400: initial; --color-neutral-500: initial;
  --color-neutral-600: initial; --color-neutral-700: initial; --color-neutral-800: initial;
  --color-neutral-900: initial; --color-neutral-950: initial;

  --color-stone-50: initial; --color-stone-100: initial; --color-stone-200: initial;
  --color-stone-300: initial; --color-stone-400: initial; --color-stone-500: initial;
  --color-stone-600: initial; --color-stone-700: initial; --color-stone-800: initial;
  --color-stone-900: initial; --color-stone-950: initial;

  --color-green-50: initial; --color-green-100: initial; --color-green-200: initial;
  --color-green-300: initial; --color-green-400: initial; --color-green-500: initial;
  --color-green-600: initial; --color-green-700: initial; --color-green-800: initial;
  --color-green-900: initial; --color-green-950: initial;

  --color-emerald-50: initial; --color-emerald-100: initial; --color-emerald-200: initial;
  --color-emerald-300: initial; --color-emerald-400: initial; --color-emerald-500: initial;
  --color-emerald-600: initial; --color-emerald-700: initial; --color-emerald-800: initial;
  --color-emerald-900: initial; --color-emerald-950: initial;

  --color-lime-50: initial; --color-lime-100: initial; --color-lime-200: initial;
  --color-lime-300: initial; --color-lime-400: initial; --color-lime-500: initial;
  --color-lime-600: initial; --color-lime-700: initial; --color-lime-800: initial;
  --color-lime-900: initial; --color-lime-950: initial;

  --color-teal-50: initial; --color-teal-100: initial; --color-teal-200: initial;
  --color-teal-300: initial; --color-teal-400: initial; --color-teal-500: initial;
  --color-teal-600: initial; --color-teal-700: initial; --color-teal-800: initial;
  --color-teal-900: initial; --color-teal-950: initial;

  --color-blue-50: initial; --color-blue-100: initial; --color-blue-200: initial;
  --color-blue-300: initial; --color-blue-400: initial; --color-blue-500: initial;
  --color-blue-600: initial; --color-blue-700: initial; --color-blue-800: initial;
  --color-blue-900: initial; --color-blue-950: initial;

  /* ========================================================================
   * TIPOGRAFÍAS OFICIALES — Anton, Bebas Neue, Outfit, Geist Mono
   * ======================================================================== */
  --font-sans: var(--font-sans, "Outfit"), "IBM Plex Sans", sans-serif;
  --font-display: var(--font-display, "Anton SC"), "Anton", sans-serif;
  --font-subheading: var(--font-subheading, "Bebas Neue"), sans-serif;
  --font-mono: var(--font-mono, "Geist Mono"), monospace;

  --text-2xs: 0.625rem;
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --text-2xl: 1.5rem;
  --text-3xl: 1.875rem;
  --text-4xl: 2.25rem;
  --text-5xl: 3rem;
  --text-6xl: 3.75rem;
  --text-7xl: 4.5rem;
  --text-8xl: 6rem;
  --text-9xl: 9rem;

  --leading-hero: 0.8;
  --leading-none: 1;
  --leading-tight: 1.25;
  --leading-relaxed: 1.625;

  --tracking-tighter: -0.05em;
  --tracking-tight: -0.025em;
  --tracking-normal: 0em;
  --tracking-wide: 0.025em;
  --tracking-wider: 0.05em;
  --tracking-widest: 0.1em;
  --tracking-mega: 0.2em;

  --spacing-section-y: 6rem;
  --spacing-section-y-tight: 3rem;
  --spacing-container-max: 80rem;
  --spacing-control-sm: 2.25rem;
  --spacing-control: 2.5rem;
  --spacing-control-lg: 2.75rem;
  --spacing-control-xl: 3.5rem;
  --spacing-control-2xl: 4rem;

  --radius-sm: 6px;
  --radius-md: 8px;
  --radius-lg: 12px;
  --radius-xl: 16px;
  --radius-2xl: 24px;
  --radius-3xl: 32px;
  --radius-4xl: 40px;
  --radius-full: 9999px;

  /* ========================================================================
   * SOMBRAS TEÑIDAS — tope #0950F6 / #FFEC01 — NUNCA grises/negras
   * ======================================================================== */
  --shadow-xs: 0 1px 2px rgba(9, 80, 246, 0.04);
  --shadow-sm: 0 2px 4px rgba(9, 80, 246, 0.06), 0 1px 2px rgba(9, 80, 246, 0.03);
  --shadow-md: 0 4px 8px rgba(9, 80, 246, 0.08), 0 2px 4px rgba(9, 80, 246, 0.04);
  --shadow-lg: 0 8px 16px rgba(9, 80, 246, 0.1), 0 4px 8px rgba(9, 80, 246, 0.06);
  --shadow-xl: 0 16px 32px rgba(9, 80, 246, 0.12), 0 8px 16px rgba(9, 80, 246, 0.08);
  --shadow-2xl: 0 25px 50px -12px rgba(9, 80, 246, 0.25);

  --shadow-panel: 0 32px 120px -20px rgba(9, 80, 246, 0.15);
  --shadow-float: 0 25px 50px -12px rgba(9, 80, 246, 0.15);
  --shadow-elevated: 0 16px 40px rgba(9, 80, 246, 0.18);
  --shadow-hover-lift: 0 24px 64px rgba(9, 80, 246, 0.20);
  --shadow-antigravity-deep: 0 24px 64px rgba(9, 80, 246, 0.22);
  --shadow-ambient-elevation: 0 20px 80px rgba(9, 80, 246, 0.18);

  --shadow-accent: 0 12px 40px -6px rgba(255, 236, 1, 0.3);
  --shadow-accent-hover: 0 6px 25px rgba(255, 236, 1, 0.4);
  --shadow-accent-sm: 0 2px 4px rgba(255, 236, 1, 0.15);
  --shadow-accent-md: 0 4px 8px rgba(255, 236, 1, 0.2);
  --shadow-glow-blue: 0 0 25px rgba(9, 80, 246, 0.35);
  --shadow-glow-yellow: 0 0 25px rgba(255, 241, 46, 0.45);
  --shadow-cta-glow: 0 0 28px rgba(255, 236, 1, 0.45), 0 8px 24px rgba(9, 80, 246, 0.18);

  --animate-float-slow: float-slow 6s ease-in-out infinite;
  --animate-pulse-subtle: pulse-subtle 2s ease-in-out infinite;
  --animate-border-pulse: border-pulse 2s ease-in-out infinite;
  --animate-shimmer: shimmer 2.5s ease-in-out infinite;
  --animate-counter-up: counter-up 0.6s ease-out;
  --animate-logos-scroll: marquee-left 30s linear infinite;

  /* ========================================================================
   * DEPRECADO: alias temporales, se borran en la fase 3
   * Cada alias apunta al canónico con var(), NUNCA a un hex.
   * ======================================================================== */
  --color-brand-navy: var(--color-brand-blue-700);
  --color-brand-blue-deep: var(--color-brand-blue-700);
  --color-brand-blue-ink: var(--color-brand-blue-700);
  --color-brand-dark: var(--color-brand-blue-700);
  --color-brand-white-50: var(--color-white);
}

@keyframes float-slow { 0%, 100% { transform: translateY(0); } 50% { transform: translateY(-8px); } }
@keyframes pulse-subtle { 0%, 100% { opacity: 1; } 50% { opacity: 0.8; } }
@keyframes border-pulse { 0%, 100% { border-color: rgba(9,80,246,0.2); } 50% { border-color: rgba(9,80,246,0.4); } }
@keyframes shimmer { 0% { background-position: -200% 0; } 100% { background-position: 200% 0; } }
@keyframes counter-up { from { opacity: 0; transform: translateY(8px); } to { opacity: 1; transform: translateY(0); } }

body {
  font-family: var(--font-sans);
  background-color: var(--surface-page);
  color: var(--text-body);
}

@utility font-display {
  font-family: var(--font-display);
  text-transform: uppercase;
  line-height: 0.9;
  letter-spacing: -0.05em;
  text-wrap: balance;
}

@utility font-subheading {
  font-family: var(--font-subheading);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

@utility font-mono {
  font-family: var(--font-mono);
  font-variant-numeric: tabular-nums;
}

/* Double-Bezel - Firma geométrica oficial */
@utility double-bezel-outer {
  background-color: color-mix(in srgb, var(--color-brand-blue-50) 80%, transparent);
  border: 1px solid var(--color-brand-blue-100);
  padding: 0.5rem;
  border-radius: var(--radius-xl);
  box-shadow: var(--shadow-float);
  transition: border-color 0.3s cubic-bezier(0.25,1,0.5,1), box-shadow 0.3s cubic-bezier(0.25,1,0.5,1);
  &:hover { border-color: var(--color-brand-blue-300); box-shadow: var(--shadow-antigravity-deep); }
}
@utility double-bezel-inner {
  background-color: var(--color-white);
  border-radius: var(--radius-lg);
  box-shadow: inset 0 2px 4px rgba(9,80,246,0.06);
  border: 1px solid color-mix(in srgb, var(--color-brand-blue-50) 50%, transparent);
}

/* CTA Nested Pill - Oficial: solo estructura (layout, tipografía, easing).
 * El color (fondo, texto, borde, sombra) lo define el variant del componente.
 */
@utility cta-nested-pill {
  display: inline-flex;
  align-items: center;
  justify-content: space-between;
  border-radius: var(--radius-full);
  font-family: var(--font-subheading);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  font-weight: 700;
  padding: 0.75rem 1.5rem;
  min-height: 56px;
  transition: transform 0.25s cubic-bezier(0.25,1,0.5,1), background-color 0.25s cubic-bezier(0.25,1,0.5,1), border-color 0.25s cubic-bezier(0.25,1,0.5,1), box-shadow 0.25s cubic-bezier(0.25,1,0.5,1);
  &:hover { transform: translateY(-1px); }
  &:active { transform: scale(0.98); }
}
@utility cta-nested-icon {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: var(--radius-full);
  width: 2.5rem;
  height: 2.5rem;
  margin-left: 0.75rem;
  background-color: rgba(9,80,246,0.1);
  transition: transform 0.25s;
  .group:hover & { transform: translateX(4px); }
}

@utility text-display {
  font-family: var(--font-display);
  font-size: clamp(3rem, 5vw, 4.5rem);
  line-height: 0.85;
  letter-spacing: -0.05em;
  text-wrap: balance;
  text-transform: uppercase;
}
@utility text-h1 {
  font-family: var(--font-display);
  font-size: clamp(2.25rem, 4vw, 3rem);
  line-height: 0.9;
  letter-spacing: -0.025em;
  text-wrap: balance;
  text-transform: uppercase;
}
@utility text-h2 {
  font-family: var(--font-display);
  font-size: clamp(1.75rem, 3vw, 2.25rem);
  line-height: 0.9;
  letter-spacing: -0.02em;
  text-wrap: balance;
  text-transform: uppercase;
}

@utility kinetic-font-stretch {
  display: inline-block;
  transition: transform 0.4s cubic-bezier(0.25,1,0.5,1), letter-spacing 0.4s;
  transform-origin: left;
  &:hover { transform: scaleX(1.08); letter-spacing: 0.02em; }
}

/* V2 Marquee Flotante */
@keyframes marquee-left { from { transform: translateX(0); } to { transform: translateX(-50%); } }
@keyframes marquee-right { from { transform: translateX(-50%); } to { transform: translateX(0); } }

/* Motion compartido de heroes (2026-09) */
@keyframes radar { from { transform: rotate(0deg); } to { transform: rotate(360deg); } }
@keyframes floaty {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-10px); }
}
@keyframes shuttle {
  from { transform: translateX(0); }
  to { transform: translateX(100%); }
}
@keyframes draw {
  from { stroke-dashoffset: var(--draw-len, 1200); }
  to { stroke-dashoffset: 0; }
}
@keyframes pulse-ring {
  0% { transform: translate(-50%, -50%) scale(0.6); opacity: 0.9; }
  100% { transform: translate(-50%, -50%) scale(3.2); opacity: 0; }
}
@keyframes roundtrip {
  0% { transform: translateX(0); }
  44% { transform: translateX(100%); }
  56% { transform: translateX(100%); }
  100% { transform: translateX(0); }
}

@utility animate-radar { animation: radar 6s linear infinite; }
@utility animate-floaty { animation: floaty 5s ease-in-out infinite; }
@utility animate-road { animation: marquee-left 3.5s linear infinite; }
@utility animate-shuttle {
  animation: shuttle 5s cubic-bezier(0.45, 0, 0.55, 1) infinite alternate;
}
@utility animate-draw { animation: draw 2.4s cubic-bezier(0.25,1,0.5,1) forwards; }
@utility animate-pulse-ring {
  animation: pulse-ring 3.2s cubic-bezier(0.25, 1, 0.5, 1) infinite;
}
@utility animate-roundtrip {
  animation: roundtrip 4.8s cubic-bezier(0.45, 0, 0.55, 1) infinite;
}
@keyframes grow-x {
  from { transform: scaleX(0); }
  to { transform: scaleX(1); }
}
@utility animate-grow-x {
  animation: grow-x 1.1s cubic-bezier(0.25, 1, 0.5, 1) forwards;
  transform-origin: left center;
}

@utility animate-marquee-left { animation: marquee-left 36s linear infinite; }
@utility animate-marquee-right { animation: marquee-right 42s linear infinite; }
@utility is-paused { animation-play-state: paused !important; }
@utility no-scrollbar { &::-webkit-scrollbar { display: none; } scrollbar-width: none; }

@media (prefers-reduced-motion: reduce) {
  .animate-radar, .animate-floaty, .animate-road, .animate-shuttle, .animate-draw, .animate-roundtrip, .animate-pulse-ring, .animate-grow-x, .animate-marquee-left, .animate-marquee-right {
    animation: none !important;
  }
  .animate-draw { stroke-dashoffset: 0 !important; }
  .animate-grow-x { transform: scaleX(1) !important; }
  .animate-pulse-ring { opacity: 0 !important; }
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.01ms !important;
  }
}

```

### Root Layout (src/app/layout.tsx) (`src/app/layout.tsx`)

```tsx
import type { Metadata } from 'next';
import { Outfit, Anton, Bebas_Neue, Geist_Mono } from 'next/font/google';
import Script from 'next/script';
import { MotionConfig } from 'motion/react';
import './globals.css';
import ClientLayout from '@/components/ClientLayout';

const outfit = Outfit({
  subsets: ['latin'],
  variable: '--font-sans',
  display: 'swap',
  preload: true,
});

const anton = Anton({
  weight: '400',
  subsets: ['latin'],
  variable: '--font-display',
  display: 'swap',
  preload: true,
});

const bebasNeue = Bebas_Neue({
  weight: '400',
  subsets: ['latin'],
  variable: '--font-subheading',
  display: 'swap',
  preload: true,
});

const geistMono = Geist_Mono({
  subsets: ['latin'],
  variable: '--font-mono',
  display: 'swap',
  preload: true,
});

const baseUrl = 'https://www.enviosdosruedas.com';

export const metadata: Metadata = {
  metadataBase: new URL(baseUrl),
  title: {
    default: 'Mensajería en moto en Mar del Plata | Envíos DosRuedas',
    template: '%s | Envíos DosRuedas',
  },
  description: 'Mensajería en moto y logística e-commerce en Mar del Plata. Express en franja de 3 hs a elección, Mercado Envíos Flex en el día y LowCost para comercios y particulares.',
  authors: [{ name: 'Envíos DosRuedas' }],
  creator: 'Envíos DosRuedas',
  publisher: 'Envíos DosRuedas',
  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      'max-video-preview': -1,
      'max-image-preview': 'large',
      'max-snippet': -1,
    },
  },
  openGraph: {
    type: 'website',
    locale: 'es_AR',
    url: baseUrl,
    siteName: 'Envíos DosRuedas',
    title: 'Mensajería en moto en Mar del Plata | Envíos DosRuedas',
    description: 'La solución logística y última milla de mayor confianza en Mar del Plata. Envíos Express, MercadoLibre Flex, ruteo eficiente y cadetería inteligente.',
    images: [
      {
        url: `${baseUrl}/og-image.jpg`,
        width: 1200,
        height: 630,
        alt: 'Envíos DosRuedas - Logística y Mensajería en Mar del Plata',
      },
    ],
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Mensajería en moto en Mar del Plata | Envíos DosRuedas',
    description: 'La solución logística y última milla de mayor confianza en Mar del Plata.',
    images: [`${baseUrl}/og-image.jpg`],
    creator: '@enviosdosruedas',
  },
  verification: {
    google: ['RKKz8Z6gsm6k3099W3s-xs7G6LTSQQNHpBs_iWfIQnM'],
  },
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html
      lang="es"
      className={`${outfit.variable} ${anton.variable} ${bebasNeue.variable} ${geistMono.variable} scroll-smooth`}
      data-scroll-behavior="smooth"
      suppressHydrationWarning
    >
      <head>
        <link rel="preconnect" href="https://www.googletagmanager.com" crossOrigin="anonymous" />
        <link rel="dns-prefetch" href="https://www.googletagmanager.com" />
        <link rel="dns-prefetch" href="https://wa.me" />
        <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
        <script
          type="application/ld+json"
          dangerouslySetInnerHTML={{
            __html: JSON.stringify({
              '@context': 'https://schema.org',
              '@graph': [
                {
                  '@type': 'Organization',
                  name: 'Envíos DosRuedas',
                  url: baseUrl,
                  logo: `${baseUrl}/logo-envios-simplified.webp`,
                  sameAs: [
                    'https://www.instagram.com/enviosdosruedas',
                    'https://www.facebook.com/enviosdosruedas',
                  ],
                  contactPoint: {
                    '@type': 'ContactPoint',
                    telephone: '+54-223-660-2699',
                    contactType: 'customer service',
                    availableLanguage: 'Spanish',
                    areaServed: 'AR',
                  },
                },
                {
                  '@type': 'LocalBusiness',
                  '@id': `${baseUrl}#localbusiness`,
                  name: 'Envíos DosRuedas',
                  description: 'Mensajería y logística e-commerce en Mar del Plata. Envíos Express en franja de 3 hs a elección, LowCost, Mercado Envíos Flex y almacenamiento en Friuli 1972.',
                  url: baseUrl,
                  telephone: '+54-223-660-2699',
                  email: 'matiascejas@enviosdosruedas.com',
                  image: `${baseUrl}/og-image.jpg`,
                  hasMap: 'https://maps.google.com/?q=Friuli+1972,+Mar+del+Plata',
                  address: {
                    '@type': 'PostalAddress',
                    streetAddress: 'Friuli 1972',
                    addressLocality: 'Mar del Plata',
                    addressRegion: 'Buenos Aires',
                    postalCode: '7600',
                    addressCountry: 'AR',
                  },
                  geo: {
                    '@type': 'GeoCoordinates',
                    latitude: -38.0055,
                    longitude: -57.5426,
                  },
                  openingHoursSpecification: [
                    {
                      '@type': 'OpeningHoursSpecification',
                      dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'],
                      opens: '09:00',
                      closes: '18:00',
                    },
                    {
                      '@type': 'OpeningHoursSpecification',
                      dayOfWeek: ['Saturday'],
                      opens: '10:00',
                      closes: '15:00',
                    },
                  ],
                  areaServed: { '@type': 'City', name: 'Mar del Plata' },
                  priceRange: '$$',
                  currenciesAccepted: 'ARS',
                  paymentAccepted: 'Cash, Credit Card, Transfer, MercadoPago',
                },
              ],
            }, null, 2)
          }}
        />
        <Script src="https://www.googletagmanager.com/gtag/js?id=AW-17510443994" strategy="lazyOnload" />
        <Script id="google-tag-init" strategy="lazyOnload">
          {`
            window.dataLayer = window.dataLayer || [];
            function gtag(){dataLayer.push(arguments);}
            gtag('js', new Date());
            gtag('config', 'AW-17510443994');
            gtag('config', 'G-LSLQ3RJ8WT');
          `}
        </Script>
      </head>
      <body className="bg-brand-white text-brand-ink font-sans antialiased selection:bg-brand-yellow selection:text-brand-blue min-h-dvh flex flex-col" suppressHydrationWarning>
        <MotionConfig reducedMotion="user">
          <ClientLayout>{children}</ClientLayout>
        </MotionConfig>
      </body>
    </html>
  );
}

```

### Client Layout (src/components/ClientLayout.tsx) (`src/components/ClientLayout.tsx`)

```tsx
'use client';

import React, { useEffect } from 'react';
import dynamic from 'next/dynamic';
import OptimizedHeader from './layout/OptimizedHeader';
import OptimizedFooter from './layout/OptimizedFooter';
import { captureAndPersistUtms } from '@/lib/analytics';

// CarruselRedes contains GSAP ScrollTrigger and is dynamically imported to avoid blocking FCP / TBT on initial paint
const CarruselRedes = dynamic(() => import('./layout/CarruselRedes'), {
  loading: () => <div className="w-full py-16 bg-brand-blue-500 min-h-62.5" />,
  ssr: true,
});

export default function ClientLayout({ children }: { children: React.ReactNode }) {
  useEffect(() => {
    captureAndPersistUtms();
  }, []);

  return (
    <>
      <OptimizedHeader />
      <main id="main-content" className="grow pt-18">
        {children}
      </main>
      <CarruselRedes />
      <OptimizedFooter />
    </>
  );
}

```

### Optimized Header (src/components/layout/OptimizedHeader.tsx) (`src/components/layout/OptimizedHeader.tsx`)

```tsx
'use client';

import React, { useState, useEffect, useRef, useMemo, useCallback } from 'react';
import Link from 'next/link';
import Image from 'next/image';
import dynamic from 'next/dynamic';
import { usePathname } from 'next/navigation';
import { AnimatePresence, motion, useReducedMotion, type Variants } from 'motion/react';
import {
  Menu, X, ChevronDown, Bike, ChevronRight, Phone,
  Home, Zap, TrendingDown, Clock, ShoppingBag, Info, HelpCircle, Share2, Mail,
  LayoutGrid, HandCoins, Building2, Rocket, Package, Store
} from 'lucide-react';
import { CTANestedPill } from '@/components/ui/CTANestedPill';

const MobileNav = dynamic(() => import('./MobileNav'), { ssr: false });

interface NavItem {
  label: string;
  href?: string;
  icon?: React.ComponentType<{ className?: string }>;
  dropdownItems?: { label: string; href: string; icon?: React.ComponentType<{ className?: string }> }[];
}

const EASE_MOUNT = { duration: 0.45, ease: [0.25, 0.8, 0.25, 1] } as const;

// NAV ITEMS - Static data, move outside component to avoid recreation on every render
const NAV_ITEMS: NavItem[] = [
  { label: 'Inicio', href: '/', icon: Home },
  {
    label: 'Servicios',
    icon: Bike,
    dropdownItems: [
      { label: 'Todos los Servicios', href: '/servicios', icon: LayoutGrid },
      { label: 'Envíos Express', href: '/servicios/envios-express', icon: Zap },
      { label: 'Envíos LowCost', href: '/servicios/envios-lowcost', icon: TrendingDown },
      { label: 'Envíos Flex (MeLi)', href: '/servicios/enviosflex', icon: Clock },
      { label: 'Cuenta Corriente Flexible', href: '/servicios/empresas-cuenta-corriente', icon: Building2 },
      { label: 'E-commerce 24HS', href: '/servicios#ecommerce-24hs', icon: Package },
      { label: 'E-commerce Same Day', href: '/servicios/deposito-fulfillment', icon: Store },
    ],
  },
  {
    label: 'Nosotros',
    icon: Info,
    dropdownItems: [
      { label: 'Sobre Nosotros', href: '/nosotros/sobre-nosotros', icon: Info },
      { label: 'Preguntas Frecuentes', href: '/nosotros/preguntas-frecuentes', icon: HelpCircle },
      { label: 'Nuestras Redes', href: '/nosotros/nuestras-redes', icon: Share2 },
    ],
  },
  { label: 'Contacto', href: '/contacto', icon: Mail },
];

export default function OptimizedHeader() {
  const [isOpen, setIsOpen] = useState(false);
  const [activeDropdown, setActiveDropdown] = useState<string | null>(null);
  const [scrolled, setScrolled] = useState(false);
  const pathname = usePathname();
  const prefersReducedMotion = useReducedMotion();
  const prevPathRef = useRef(pathname);

  // Memoize dropdown variants to avoid recreation on every render
  const dropdownContainer = useMemo<Variants>(() => ({
    hidden: { opacity: 0, y: prefersReducedMotion ? 0 : 8, scale: prefersReducedMotion ? 1 : 0.97 },
    visible: {
      opacity: 1, y: 0, scale: 1,
      transition: { type: 'spring', stiffness: 320, damping: 24, staggerChildren: prefersReducedMotion ? 0 : 0.06, delayChildren: 0.02 },
    },
    exit: { opacity: 0, y: prefersReducedMotion ? 0 : 6, scale: prefersReducedMotion ? 1 : 0.97, transition: { duration: 0.15, ease: 'easeIn' as const } },
  }), [prefersReducedMotion]);

  const dropdownItem = useMemo<Variants>(() => ({
    hidden: { opacity: 0, x: prefersReducedMotion ? 0 : -8 },
    visible: { opacity: 1, x: 0, transition: { type: 'spring', stiffness: 400, damping: 28 } },
  }), [prefersReducedMotion]);

  const handleDropdownToggle = useCallback((label: string) => {
    setActiveDropdown(prev => (prev === label ? null : label));
  }, []);

  useEffect(() => {
    const handleScroll = () => setScrolled(window.scrollY > 20);
    window.addEventListener('scroll', handleScroll, { passive: true });
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  // FIX ESLINT react-hooks/set-state-in-effect: cierra drawer al cambiar ruta sin setState sincrónico en effect
  // Usamos ref + async microtask para no ser sincrónico
  useEffect(() => {
    if (prevPathRef.current !== pathname) {
      prevPathRef.current = pathname;
      // Solo si está abierto, lo cerramos en próximo tick (no sincrónico)
      if (isOpen || activeDropdown) {
        const id = setTimeout(() => {
          setIsOpen(false);
          setActiveDropdown(null);
        }, 0);
        return () => clearTimeout(id);
      }
    }
  }, [pathname, isOpen, activeDropdown]);

  // Lock scroll robusto
  useEffect(() => {
    if (isOpen) {
      const scrollY = window.scrollY;
      document.body.style.position = 'fixed';
      document.body.style.top = `-${scrollY}px`;
      document.body.style.width = '100%';
      document.body.style.overflow = 'hidden';
      return () => {
        document.body.style.position = '';
        document.body.style.top = '';
        document.body.style.width = '';
        document.body.style.overflow = '';
        window.scrollTo(0, scrollY);
      };
    }
  }, [isOpen]);

  return (
    <>
      <header
        id="optimized-header"
        className={`fixed top-0 left-0 right-0 z-50 w-full transition-[background-color,border-color,box-shadow,padding] duration-300 ${
          scrolled ? 'bg-brand-blue-700/95 shadow-elevated border-b border-white/10 py-2.5 backdrop-blur-md' : 'bg-brand-blue-700 py-4 border-b border-transparent'
        }`}
      >
        <motion.div initial={prefersReducedMotion ? false : { opacity: 0, y: -8 }} animate={{ opacity: 1, y: 0 }} transition={EASE_MOUNT} className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
          <div className="flex items-center justify-between">
            <Link href="/" id="nav-logo-opt" className="flex items-center gap-3 group focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 rounded-xl">
              <div className="flex items-center gap-2.5">
                <motion.div className="relative w-10 h-10 shrink-0" whileHover={prefersReducedMotion ? {} : { rotate: 12, scale: 1.08 }} whileTap={prefersReducedMotion ? {} : { scale: 0.95 }} transition={{ type: 'spring', stiffness: 500, damping: 18 }}>
                  {/* `sizes` es obligatorio con `fill`: sin él Next asume 100vw y el browser
    descarga la variante de 1536px para una caja de 40x40. Medido en producción:
    25.598 bytes de los cuales 25.534 eran desperdicio (99,7%). Como lleva
    `priority`, se precarga en el critical path de todas las páginas. */}
<Image
  src="/logo-envios-simplified.webp"
  alt="Logo Envíos Dos Ruedas"
  fill
  sizes="40px"
  className="object-contain"
  priority
/>
                </motion.div>
                <span className="font-display text-2xl sm:text-3xl tracking-tight leading-none uppercase select-none flex flex-col sm:flex-row sm:gap-1 items-start sm:items-center">
                  <span className="text-white kinetic-font-stretch">Envíos</span>
                  <span className="text-brand-yellow-500 kinetic-font-stretch">DosRuedas</span>
                </span>
              </div>
            </Link>

            <nav id="desktop-nav-opt" className="hidden lg:flex items-center gap-2">
              {NAV_ITEMS.map((item) => (
                <div key={item.label} className="relative" onMouseEnter={() => item.dropdownItems && setActiveDropdown(item.label)} onMouseLeave={() => setActiveDropdown(null)}>
                  {item.href ? (
                    <Link href={item.href} className="px-4 py-2.5 rounded-xl text-base font-subheading font-bold uppercase tracking-wider text-white hover:text-brand-yellow-500 hover:bg-white/10 transition-colors">{item.label}</Link>
                  ) : (
                    <button onClick={() => handleDropdownToggle(item.label)} aria-haspopup="menu" aria-expanded={activeDropdown === item.label} className="px-4 py-2.5 rounded-xl text-base font-subheading font-bold uppercase tracking-wider text-white hover:text-brand-yellow-500 hover:bg-white/10 transition-colors flex items-center gap-1.5">
                      {item.label}<ChevronDown className={`h-4 w-4 transition-transform ${activeDropdown === item.label ? 'rotate-180' : ''}`} />
                    </button>
                  )}
                  <AnimatePresence>
                    {item.dropdownItems && activeDropdown === item.label && (
                      <motion.div variants={dropdownContainer} initial="hidden" animate="visible" exit="exit" className="absolute left-0 mt-2 w-64 bg-brand-blue-700 rounded-2xl shadow-2xl border border-white/15 py-2.5 text-white overflow-hidden z-50">
                        <div className="flex flex-col gap-1 px-2">
                          {item.dropdownItems.map((subItem) => {
                            const SubIcon = subItem.icon || ChevronRight;
                            return (
                              <motion.div key={subItem.href} variants={dropdownItem}>
                                <Link href={subItem.href} className="flex items-center gap-3 px-3 py-2.5 rounded-xl transition-colors hover:bg-white/10 text-white hover:text-brand-yellow-500 group focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500">
                                  <div className="p-1.5 rounded-lg bg-white/10 text-brand-blue-50 group-hover:bg-brand-yellow-500 group-hover:text-brand-blue-700 transition-colors shrink-0"><SubIcon className="h-4 w-4" /></div>
                                  <span className="text-base font-bold uppercase font-subheading tracking-wider leading-none">{subItem.label}</span>
                                </Link>
                              </motion.div>
                            );
                          })}
                        </div>
                      </motion.div>
                    )}
                  </AnimatePresence>
                </div>
              ))}
            </nav>

            <div className="hidden lg:flex items-center gap-5">
              <a href="tel:+542236602699" className="flex items-center gap-2 text-white hover:text-brand-yellow-500 transition-colors font-mono text-base font-bold"><Phone className="h-4 w-4 text-brand-yellow-500" /><span>223 660-2699</span></a>
              <div className="relative">
                {!(pathname === '/' || pathname.startsWith('/servicios') || pathname.startsWith('/cotizar')) && !prefersReducedMotion && (
                  <motion.span className="absolute inset-0 rounded-full bg-brand-yellow-500/25 pointer-events-none" animate={{ scale: [1, 1.18, 1], opacity: [0.6, 0, 0.6] }} transition={{ duration: 2.4, repeat: Infinity, ease: 'easeInOut', repeatDelay: 1.5 }} />
                )}
                <CTANestedPill href="/cotizar" variant={(pathname === '/' || pathname.startsWith('/servicios') || pathname.startsWith('/cotizar')) ? 'outline' : 'primary'} size="default" className={(pathname === '/' || pathname.startsWith('/servicios') || pathname.startsWith('/cotizar')) ? 'border-white/40 text-white hover:bg-white/10 hover:border-white' : ''}>Cotizá tu envío</CTANestedPill>
              </div>
            </div>

            <div className="lg:hidden flex items-center gap-3">
              <a href="tel:+542236602699" className="p-2.5 rounded-xl bg-white/10 hover:bg-white/15 text-white hover:text-brand-yellow-500 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 transition-all min-w-11 min-h-11 flex items-center justify-center" aria-label="Llamar"><Phone className="h-5 w-5 text-brand-yellow-500" /></a>
              <button onClick={() => setIsOpen(!isOpen)} id="mobile-menu-toggle-opt" className="p-2.5 rounded-xl bg-white/10 hover:bg-white/15 text-white hover:text-brand-yellow-500 focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 transition-all cursor-pointer min-w-11 min-h-11 flex items-center justify-center" aria-label={isOpen ? 'Cerrar menú' : 'Abrir menú'} aria-expanded={isOpen} aria-controls="mobile-navigation-dialog">
                <AnimatePresence mode="wait" initial={false}>
                  {isOpen ? (
                    <motion.span key="close" initial={prefersReducedMotion ? false : { rotate: -90, opacity: 0 }} animate={{ rotate: 0, opacity: 1 }} exit={prefersReducedMotion ? {} : { rotate: 90, opacity: 0 }} transition={{ duration: 0.18 }}><X className="h-6 w-6" /></motion.span>
                  ) : (
                    <motion.span key="menu" initial={prefersReducedMotion ? false : { rotate: 90, opacity: 0 }} animate={{ rotate: 0, opacity: 1 }} exit={prefersReducedMotion ? {} : { rotate: -90, opacity: 0 }} transition={{ duration: 0.18 }}><Menu className="h-6 w-6" /></motion.span>
                  )}
                </AnimatePresence>
              </button>
            </div>
          </div>
        </motion.div>
      </header>

      <AnimatePresence>{isOpen && <MobileNav isOpen={isOpen} onClose={() => setIsOpen(false)} navItems={NAV_ITEMS} activeDropdown={activeDropdown} onDropdownToggle={handleDropdownToggle} />}</AnimatePresence>
    </>
  );
}

```

### Mobile Navigation Drawer (src/components/layout/MobileNav.tsx) (`src/components/layout/MobileNav.tsx`)

```tsx
'use client';

import React, { useEffect } from 'react';
import Link from 'next/link';
import { createPortal } from 'react-dom';
import { motion, AnimatePresence, useReducedMotion } from 'motion/react';
import { ChevronDown, ChevronRight, Phone, X } from 'lucide-react';
import { CTANestedPill } from '@/components/ui';

export interface MobileNavItem {
  label: string;
  href?: string;
  icon?: React.ComponentType<{ className?: string }>;
  dropdownItems?: { label: string; href: string; icon?: React.ComponentType<{ className?: string }> }[];
}

export interface MobileNavProps {
  isOpen: boolean;
  onClose: () => void;
  navItems: MobileNavItem[];
  activeDropdown: string | null;
  onDropdownToggle: (label: string) => void;
}

const SPRING_PANEL = { type: 'spring', stiffness: 340, damping: 30 } as const;
const NAV_CONTAINER = { hidden: {}, visible: { transition: { staggerChildren: 0.07, delayChildren: 0.15 } } } as const;
const NAV_ITEM_VARIANT = { hidden: { opacity: 0, x: 24 }, visible: { opacity: 1, x: 0, transition: { type: 'spring', stiffness: 380, damping: 26 } } } as const;

// FIX ESLINT: useSyncExternalStore para mounted sin setState en effect
function useIsMounted() {
  return React.useSyncExternalStore(
    () => () => {},
    () => true,
    () => false
  );
}

export const MobileNav: React.FC<MobileNavProps> = ({ isOpen, onClose, navItems, activeDropdown, onDropdownToggle }) => {
  const prefersReducedMotion = useReducedMotion();
  const mounted = useIsMounted();
  const drawerRef = React.useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!isOpen) return;
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        e.preventDefault();
        onClose();
        return;
      }
      if (e.key === 'Tab' && drawerRef.current) {
        const focusable = drawerRef.current.querySelectorAll<HTMLElement>('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
        if (focusable.length === 0) return;
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (e.shiftKey && document.activeElement === first) {
          e.preventDefault();
          last.focus();
        } else if (!e.shiftKey && document.activeElement === last) {
          e.preventDefault();
          first.focus();
        }
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    const t = setTimeout(() => drawerRef.current?.querySelector<HTMLElement>('button, [href]')?.focus(), 80);
    return () => {
      window.removeEventListener('keydown', handleKeyDown);
      clearTimeout(t);
      document.getElementById('mobile-menu-toggle-opt')?.focus();
    };
  }, [isOpen, onClose]);

  if (!mounted) return null;

  const content = (
    <>
      <motion.div initial={{ opacity: 0 }} animate={{ opacity: 1 }} exit={{ opacity: 0 }} transition={{ duration: prefersReducedMotion ? 0 : 0.2 }} onClick={onClose} className="fixed inset-0 bg-brand-blue-700/70 backdrop-blur-md z-99 lg:hidden" />
      <motion.div
        ref={drawerRef}
        id="mobile-navigation-dialog"
        role="dialog"
        aria-modal="true"
        aria-label="Menú principal"
        initial={prefersReducedMotion ? { x: 0 } : { x: '100%' }}
        animate={{ x: 0 }}
        exit={prefersReducedMotion ? { opacity: 0 } : { x: '100%' }}
        transition={SPRING_PANEL}
        className="fixed top-0 right-0 bottom-0 z-100 flex flex-col w-full max-w-[320px] h-dvh bg-brand-blue-700 shadow-2xl border-l border-white/10 lg:hidden overscroll-contain"
      >
        <div className="flex items-center justify-between px-5 py-4 border-b border-white/10 shrink-0 h-16">
          <Link href="/" onClick={onClose} className="flex items-center gap-3 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50 rounded-lg">
            <span className="font-display text-xl tracking-tight uppercase select-none flex flex-col items-start leading-none">
              <span className="text-white">Envíos</span>
              <span className="text-brand-yellow-500">DosRuedas</span>
            </span>
          </Link>
          <motion.button onClick={onClose} whileHover={prefersReducedMotion ? {} : { scale: 1.08, rotate: 90 }} whileTap={prefersReducedMotion ? {} : { scale: 0.92 }} transition={{ type: 'spring', stiffness: 500, damping: 20 }} className="p-2.5 rounded-xl bg-white/10 hover:bg-white/15 text-white hover:text-brand-yellow-500 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50 transition-colors cursor-pointer min-w-11 min-h-11 flex items-center justify-center" aria-label="Cerrar menú">
            <X className="h-5 w-5" />
          </motion.button>
        </div>

        <div className="flex-1 overflow-y-auto overscroll-contain px-5 py-6 space-y-6">
          <motion.nav className="space-y-2" variants={prefersReducedMotion ? {} : NAV_CONTAINER} initial="hidden" animate="visible">
            {navItems.map((item) => (
              <motion.div key={item.label} variants={prefersReducedMotion ? {} : NAV_ITEM_VARIANT} className="border-b border-white/10 pb-2.5 last:border-b-0 last:pb-0">
                {item.href ? (
                  <Link href={item.href} onClick={onClose} className="flex items-center gap-3.5 py-2.5 px-3 rounded-xl text-xl font-subheading tracking-wider uppercase text-white hover:text-brand-yellow-500 hover:bg-white/5 transition-all font-bold min-h-12 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50">
                    {item.icon && <item.icon className="h-5 w-5 text-brand-yellow-500 shrink-0" />}
                    <span>{item.label}</span>
                  </Link>
                ) : (
                  <div>
                    <button onClick={() => onDropdownToggle(item.label)} className="w-full text-left py-2.5 px-3 rounded-xl text-xl font-subheading tracking-wider uppercase flex items-center justify-between text-white hover:bg-white/5 font-bold cursor-pointer transition-all min-h-12 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50">
                      <span className="flex items-center gap-3.5">{item.icon && <item.icon className="h-5 w-5 text-brand-yellow-500 shrink-0" />}<span>{item.label}</span></span>
                      <motion.span animate={{ rotate: activeDropdown === item.label ? 180 : 0 }} transition={{ type: 'spring', stiffness: 400, damping: 25 }}><ChevronDown className="h-5 w-5 text-brand-yellow-500 shrink-0" /></motion.span>
                    </button>
                    <AnimatePresence>
                      {item.dropdownItems && activeDropdown === item.label && (
                        <motion.div initial={{ opacity: 0, height: 0 }} animate={{ opacity: 1, height: 'auto' }} exit={{ opacity: 0, height: 0 }} transition={prefersReducedMotion ? { duration: 0 } : { type: 'spring', stiffness: 340, damping: 28 }} className="pl-4 pr-1 py-2 flex flex-col gap-1 overflow-hidden">
                          {item.dropdownItems.map((subItem, idx) => {
                            const SubIcon = subItem.icon || ChevronRight;
                            return (
                              <motion.div key={subItem.href} initial={prefersReducedMotion ? {} : { opacity: 0, x: 12 }} animate={{ opacity: 1, x: 0 }} transition={{ delay: idx * 0.05, type: 'spring', stiffness: 380, damping: 26 }}>
                                <Link href={subItem.href} onClick={onClose} className="flex items-center gap-3 py-2 px-3 rounded-xl text-base font-subheading uppercase tracking-wider font-bold text-brand-blue-50/90 hover:text-brand-yellow-500 hover:bg-white/10 transition-all min-h-10.5 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50">
                                  <div className="p-1 rounded-lg bg-white/10 text-brand-yellow-500 shrink-0"><SubIcon className="h-4 w-4" /></div><span>{subItem.label}</span>
                                </Link>
                              </motion.div>
                            );
                          })}
                        </motion.div>
                      )}
                    </AnimatePresence>
                  </div>
                )}
              </motion.div>
            ))}
          </motion.nav>
        </div>

        <div className="p-5 border-t border-white/10 space-y-4 shrink-0 bg-brand-blue-700 backdrop-blur-md mt-auto">
          <a href="tel:+542236602699" className="flex items-center justify-center gap-2.5 py-3 px-4 rounded-xl bg-white/10 border border-white/5 text-white hover:text-brand-yellow-500 font-mono text-sm font-bold transition-all min-h-11 focus:outline-none focus:ring-2 focus:ring-brand-yellow-500/50"><Phone className="h-4 w-4 text-brand-yellow-500" /><span>+54 223 660-2699</span></a>
          <CTANestedPill href="/cotizar" variant="primary" size="large" className="w-full justify-center min-h-11 py-3.5" onClick={onClose}>Cotizá tu envío</CTANestedPill>
        </div>
      </motion.div>
    </>
  );

  return createPortal(content, document.body);
};

export default MobileNav;

```

### Carrusel Redes (src/components/layout/CarruselRedes.tsx) (`src/components/layout/CarruselRedes.tsx`)

```tsx
'use client';

import React, { useEffect, useRef } from 'react';
import { FaInstagram, FaFacebook, FaWhatsapp } from 'react-icons/fa';
import { ArrowUpRight } from 'lucide-react';
import { useReducedMotion } from 'motion/react';
import gsap from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';

export default function CarruselRedes() {
  const sectionRef = useRef<HTMLDivElement>(null);
  const containerRef = useRef<HTMLDivElement>(null);
  const prefersReducedMotion = useReducedMotion();

  useEffect(() => {
    gsap.registerPlugin(ScrollTrigger);

    // Early return for reduced motion - no animations at all
    if (prefersReducedMotion) {
      // Ensure blocks are visible without animation
      if (containerRef.current) {
        const blocks = containerRef.current.querySelectorAll('.social-block');
        blocks.forEach((block) => {
          (block as HTMLElement).style.opacity = '1';
          (block as HTMLElement).style.transform = 'none';
        });
      }
      return;
    }

    const ctx = gsap.context(() => {
      if (containerRef.current) {
        const blocks = containerRef.current.querySelectorAll('.social-block');
        gsap.fromTo(
          blocks,
          {
            y: 50,
            opacity: 0,
            scale: 0.96,
          },
          {
            y: 0,
            opacity: 1,
            scale: 1,
            stagger: 0.15,
            duration: 0.8,
            ease: 'power3.out',
            scrollTrigger: {
              trigger: containerRef.current,
              start: 'top 85%',
              once: true,
            },
          }
        );
      }
    }, sectionRef);

    return () => ctx.revert();
  }, [prefersReducedMotion]);

  const networks = [
    {
      id: 'facebook',
      name: 'FACEBOOK',
      handle: 'Envíos DosRuedas',
      desc: 'Seguí nuestro día a día, novedades operativas y la comunidad comercial en Mar del Plata.',
      action: 'SEGUIR COMUNIDAD',
      url: 'https://www.facebook.com/share/1RnSzyweir/',
      icon: FaFacebook,
      badgeText: 'FACEBOOK OFICIAL',
      // Estética propia Facebook (Royal Classic Blue)
      cardBg: 'bg-[#1877F2]/10 hover:bg-[#1877F2]/15',
      cardBorder: 'border-[#1877F2]/30 hover:border-[#1877F2]/70',
      badgeBg: 'bg-[#1877F2]/20 text-brand-blue-50 border-[#1877F2]/40',
      iconBoxBg: 'bg-[#0B5ED7] text-white shadow-lg shadow-[#1877F2]/40',
      handleColor: 'text-brand-blue-50',
      watermarkColor: 'text-[#1877F2]/10 group-hover:text-[#1877F2]/20',
      btnBg: 'bg-[#0B5ED7] hover:bg-[#0A4FC0] text-white shadow-md shadow-[#1877F2]/30',
      btnIconBg: 'bg-white/20 text-white',
      glow: 'from-[#1877F2]/20 to-transparent',
    },
    {
      id: 'instagram',
      name: 'INSTAGRAM',
      handle: '@enviosdosruedas',
      desc: 'Mirá el detrás de escena de nuestros riders y la flota recorriendo las calles de MDQ.',
      action: 'VER CONTENIDO',
      url: 'https://www.instagram.com/enviosdosruedas/',
      icon: FaInstagram,
      badgeText: 'INSTAGRAM MDQ',
      // Estética propia Instagram (Gradient Sunset & Pink/Purple)
      cardBg: 'bg-gradient-to-br from-[#833AB4]/10 via-[#FD1D1D]/10 to-[#F77737]/10 hover:from-[#833AB4]/15 hover:via-[#FD1D1D]/15 hover:to-[#F77737]/15',
      cardBorder: 'border-[#E1306C]/30 hover:border-[#E1306C]/70',
      badgeBg: 'bg-linear-to-r from-[#833AB4]/20 via-[#FD1D1D]/20 to-[#F77737]/20 text-brand-blue-50 border-[#E1306C]/40',
      iconBoxBg: 'bg-linear-to-tr from-[#F56040] via-[#FD1D1D] to-[#833AB4] text-white shadow-lg shadow-[#E1306C]/40',
      handleColor: 'text-brand-blue-50',
      watermarkColor: 'text-[#E1306C]/10 group-hover:text-[#E1306C]/20',
      btnBg: 'bg-linear-to-r from-[#833AB4] via-[#FD1D1D] to-[#F77737] hover:opacity-95 text-white shadow-md shadow-[#FD1D1D]/30',
      btnIconBg: 'bg-white/20 text-white',
      glow: 'from-[#E1306C]/20 to-transparent',
    },
    {
      id: 'whatsapp',
      name: 'WHATSAPP',
      handle: '+54 223 660-2699',
      desc: 'Escribinos directamente para consultas, contrataciones o soporte express al toque.',
      action: 'INICIAR CHAT',
      url: 'https://wa.me/542236602699',
      icon: FaWhatsapp,
      badgeText: 'WHATSAPP DIRECTO',
      // Estética oficial Envíos DosRuedas (Brand Yellow & Navy Blue)
      cardBg: 'bg-brand-yellow-500/10 hover:bg-brand-yellow-500/15',
      cardBorder: 'border-brand-yellow-500/30 hover:border-brand-yellow-500/70',
      badgeBg: 'bg-brand-yellow-500/20 text-brand-yellow-500 border-brand-yellow-500/40',
      iconBoxBg: 'bg-brand-yellow-500 text-brand-blue-900 shadow-lg shadow-brand-yellow-500/30',
      handleColor: 'text-brand-yellow-400',
      watermarkColor: 'text-brand-yellow-500/10 group-hover:text-brand-yellow-500/20',
      btnBg: 'bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 font-bold shadow-md shadow-brand-yellow-500/30',
      btnIconBg: 'bg-transparent text-brand-blue-900',
      glow: 'from-brand-yellow-500/20 to-transparent',
    },
  ];

  return (
    <section
      ref={sectionRef}
      id="carrusel-redes"
      suppressHydrationWarning
      className="py-20 md:py-32 bg-brand-blue border-y border-white/10 relative overflow-hidden font-sans select-none"
    >
      {/* Background Decorative Mesh & Depth Highlights */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(255,236,1,0.08),transparent_50%)] pointer-events-none" />
      <div className="absolute top-0 left-1/4 w-100 h-100 bg-brand-blue-500/10 rounded-full blur-[100px] pointer-events-none" />

      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* Header Segment */}
        <div className="text-center max-w-3xl mx-auto mb-16 space-y-4">
          <span className="px-4 py-1.5 bg-brand-yellow-500 text-brand-blue-900 rounded-full text-xs font-bold tracking-widest inline-block font-subheading uppercase shadow-accent-sm">
            Nuestra Comunidad Digital
          </span>
          
          <h2 className="text-white text-4xl sm:text-5xl lg:text-6xl font-display uppercase tracking-tight leading-[0.95] text-center">
            SEGUÍ NUESTRO <span className="text-brand-yellow-500">MOVIMIENTO</span>
          </h2>

          <p className="text-brand-blue-50 text-sm sm:text-base leading-relaxed font-sans max-w-2xl mx-auto opacity-90">
            Sumate a nuestros canales digitales y enterate al toque de todas las novedades operativas en Mar del Plata.
          </p>
          <div className="h-0.5 w-20 bg-brand-yellow-500 mx-auto rounded-full mt-4" />
        </div>

        {/* Networks Grid: 3 Unique Branded Cards */}
        <div
          ref={containerRef}
          className="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 w-full"
        >
          {networks.map((net) => {
            const Icon = net.icon;

            return (
              <div
                key={net.id}
                className={`social-block group relative rounded-2xl p-2 transition-[transform,border-color,box-shadow] duration-300 border ${net.cardBorder} bg-brand-blue/80 backdrop-blur-md hover:-translate-y-1.5 shadow-xl`}
              >
                {/* Internal Glow on Hover */}
                <div className={`absolute inset-0 rounded-2xl bg-linear-to-b ${net.glow} opacity-0 group-hover:opacity-100 transition-opacity duration-300 pointer-events-none`} />

                <div className={`relative rounded-xl p-6 sm:p-7 flex flex-col justify-between h-97.5 md:h-107.5 overflow-hidden ${net.cardBg} border border-white/10 transition-colors`}>
                  
                  {/* Background Watermark Icon that enlarges and tilts on hover */}
                  <div className={`absolute -right-8 -bottom-8 ${net.watermarkColor} transition-transform duration-500 ease-out group-hover:scale-125 group-hover:-rotate-12 pointer-events-none select-none`}>
                    <Icon className="w-56 h-56" />
                  </div>

                  {/* Top Area: Badge & Branded Icon Box */}
                  <div className="z-10 text-left space-y-4">
                    <div className="flex items-center justify-between">
                      <span className={`text-2xs font-bold tracking-widest px-3 py-1 rounded-full uppercase font-subheading border ${net.badgeBg}`}>
                        {net.badgeText}
                      </span>

                      <div className={`w-11 h-11 rounded-xl flex items-center justify-center transition-transform duration-300 group-hover:scale-110 ${net.iconBoxBg}`}>
                        <Icon className="w-5 h-5" />
                      </div>
                    </div>

                    <div>
                      <h3 className="font-display text-3xl sm:text-4xl uppercase tracking-tight leading-none text-white">
                        {net.name}
                      </h3>
                      <p className={`font-mono text-xs font-bold mt-1.5 ${net.handleColor}`}>
                        {net.handle}
                      </p>
                    </div>

                    <p className="font-sans text-xs sm:text-sm leading-relaxed text-brand-blue-50/90 font-light">
                      {net.desc}
                    </p>
                  </div>

                  {/* Bottom Action Area: Custom CTA Button per Network */}
                  <div className="z-10 pt-4 border-t border-white/10">
                    <a
                      href={net.url}
                      target="_blank"
                      rel="noopener noreferrer"
                      className={`w-full inline-flex items-center justify-between font-subheading font-bold uppercase tracking-wider text-xs sm:text-sm px-5 py-3 rounded-full transition-colors duration-200 group/btn ${net.btnBg}`}
                    >
                      <span>{net.action}</span>
                      <span className={`w-7 h-7 rounded-full flex items-center justify-center shrink-0 ml-2 transition-transform duration-200 group-hover/btn:translate-x-1 ${net.btnIconBg}`}>
                        <ArrowUpRight className="w-4 h-4" />
                      </span>
                    </a>
                  </div>

                </div>
              </div>
            );
          })}
        </div>

      </div>
    </section>
  );
}


```

### Optimized Footer (src/components/layout/OptimizedFooter.tsx) (`src/components/layout/OptimizedFooter.tsx`)

```tsx
'use client';

import React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { motion, useReducedMotion } from 'motion/react';
import {
  Phone, MapPin, Mail, Clock, ShieldCheck, ArrowUpRight,
  Zap, TrendingDown, ShoppingBag, ArrowUp, Rocket, Layers, Building2, Package, Store
} from 'lucide-react';
import { FaInstagram, FaFacebook, FaWhatsapp } from 'react-icons/fa';

// ─── Animation Variants ───────────────────────────────────────────────────────

/** Fade-up stagger container for footer columns */
const FOOTER_CONTAINER = {
  hidden: {},
  visible: {
    transition: { staggerChildren: 0.12, delayChildren: 0.1 },
  },
} as const;

/** Each column fades up */
const FOOTER_COL = {
  hidden: { opacity: 0, y: 28 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: 'spring', stiffness: 280, damping: 24 },
  },
} as const;

/** CTA Banner slides up from below */
const BANNER_VARIANT = {
  hidden: { opacity: 0, y: 40 },
  visible: {
    opacity: 1,
    y: 0,
    transition: { type: 'spring', stiffness: 260, damping: 22, delay: 0.08 },
  },
} as const;

/** Social icon spring bounce on hover */
const SOCIAL_HOVER = { y: -4, scale: 1.12 } as const;
const SOCIAL_SPRING = { type: 'spring', stiffness: 480, damping: 18 } as const;

export default function OptimizedFooter() {
  const prefersReducedMotion = useReducedMotion();

  const scrollToTop = () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  };

  return (
    <footer
      id="optimized-footer"
      className="bg-brand-blue-700 text-white border-t border-white/10 relative overflow-hidden font-sans select-none"
    >
      {/* Decorative top yellow accent bar with continuous glow */}
      <div className="h-1.5 bg-brand-yellow-500 w-full shadow-md shadow-brand-yellow-500/30" />

      {/* Atmospheric Background & Subtle Blueprint Grid Details */}
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_50%_0%,rgba(255,236,1,0.08),transparent_50%)] pointer-events-none" />
      <div className="absolute inset-0 bg-[radial-gradient(circle_at_10%_90%,rgba(9,80,246,0.5),transparent_40%)] pointer-events-none" />
      <div className="absolute inset-0 opacity-5 bg-[linear-gradient(to_right,#ffffff_1px,transparent_1px),linear-gradient(to_bottom,#ffffff_1px,transparent_1px)] bg-size-[32px_32px] pointer-events-none" />

      {/* Main Container */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-16 pb-12 relative z-10">

        {/* TOP CTA BANNER — slides up from below on scroll reveal */}
        <motion.div
          variants={prefersReducedMotion ? {} : BANNER_VARIANT}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-60px' }}
          className="mb-14 rounded-2xl bg-brand-blue/90 border border-white/15 p-6 sm:p-8 backdrop-blur-md shadow-2xl flex flex-col md:flex-row items-center justify-between gap-6"
        >
          <div className="space-y-2 text-center md:text-left">
            <div className="inline-flex items-center gap-2 px-3.5 py-1 rounded-full bg-brand-yellow-500/15 border border-brand-yellow-500/30 text-brand-yellow-500 text-xs font-subheading font-bold uppercase tracking-wider">
              <span className="w-2 h-2 rounded-full bg-brand-yellow-500 animate-ping motion-reduce:animate-none" />
              Operaciones Activas Mar del Plata 2026
            </div>
            <h3 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-white">
              ¿Tenés envíos para hoy? <span className="text-brand-yellow-500">Los entregamos a tiempo.</span>
            </h3>
            <p className="text-sm text-brand-blue-50 font-light max-w-xl">
              Cotizá online en segundos o coordiná directo con nuestro equipo logístico por WhatsApp.
            </p>
          </div>

          <div className="flex flex-col sm:flex-row items-center gap-3 w-full md:w-auto shrink-0">
            <Link
              href="/cotizar"
              className="w-full sm:w-auto cta-nested-pill bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 font-subheading font-bold uppercase tracking-wider text-sm px-6 py-3.5 rounded-full shadow-accent-sm hover:shadow-cta-glow transition-all flex items-center justify-between group min-h-12"
            >
              <span>Cotizá tu Envío</span>
              <span className="cta-nested-icon bg-brand-blue-900/10 text-brand-blue-900 h-7 w-7 rounded-full flex items-center justify-center shrink-0 ml-3 group-hover:translate-x-1 transition-transform">
                <ArrowUpRight className="h-4 w-4" />
              </span>
            </Link>

            <a
              href="https://wa.me/542236602699?text=Hola%20Envíos%20DosRuedas!%20Quiero%20hacer%20una%20consulta%20de%20envíos"
              target="_blank"
              rel="noopener noreferrer"
              aria-label="Chateá con Nosotros por WhatsApp para consultas de envíos"
              className="w-full sm:w-auto inline-flex items-center justify-center gap-2 bg-white/10 hover:bg-white/20 text-white border border-white/20 hover:border-white/40 font-subheading font-bold uppercase tracking-wider text-sm px-5 py-3.5 rounded-full transition-all min-h-12"
            >
              <FaWhatsapp className="h-4 w-4 text-brand-yellow-500" />
              <span>Chateá con Nosotros</span>
            </a>
          </div>
        </motion.div>

        {/* MID SECTION: fade-up stagger per column on scroll reveal */}
        <motion.div
          className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-12 gap-10 lg:gap-12 items-start"
          variants={prefersReducedMotion ? {} : FOOTER_CONTAINER}
          initial="hidden"
          whileInView="visible"
          viewport={{ once: true, margin: '-60px' }}
        >

          {/* COLUMN 1: Brand details & Socials (4 Cols) */}
          <motion.div
            variants={prefersReducedMotion ? {} : FOOTER_COL}
            className="lg:col-span-4 space-y-6"
          >
            <Link href="/" className="flex items-center gap-3.5 group w-fit focus:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 rounded-xl">
              <div className="relative w-11 h-11 bg-white/10 p-1.5 rounded-xl border border-white/15 group-hover:scale-105 transition-all duration-300 shrink-0 flex items-center justify-center">
                <Image
                  src="/logo-envios-simplified.webp"
                  alt="Logo Envíos DosRuedas"
                  width={32}
                  height={32}
                  className="object-contain"
                />
              </div>
              <div className="flex flex-col leading-none">
                <span className="font-display text-2xl sm:text-3xl tracking-tight uppercase select-none text-white">
                  Envíos <span className="text-brand-yellow-500">DosRuedas</span>
                </span>
                <span className="text-2xs font-mono text-brand-blue-50 tracking-widest uppercase mt-0.5 opacity-90">
                  Tu solución confiable · Mar del Plata
                </span>
              </div>
            </Link>

            <p className="text-brand-blue-50 text-sm leading-relaxed max-w-sm font-light">
              Con más de 7 años de trayectoria en Mar del Plata, transformamos el despacho de tus productos en un motor de crecimiento para emprendedores, PyMEs y comercios locales con flota propia y compromiso humano.
            </p>

            <div className="space-y-3 pt-2">
              <span className="block text-xs font-bold text-brand-yellow-500 uppercase tracking-widest font-subheading">
                Canales Oficiales
              </span>
              <div className="flex flex-wrap items-center gap-3">
                {/* Instagram — spring bounce */}
                <motion.div
                  whileHover={prefersReducedMotion ? {} : SOCIAL_HOVER}
                  transition={SOCIAL_SPRING}
                  className="inline-block"
                >
                  <Link
                    href="/nosotros/nuestras-redes"
                    className="h-10 w-10 rounded-xl bg-white/10 hover:bg-brand-yellow-500 text-white hover:text-brand-blue-900 flex items-center justify-center transition-colors duration-200 border border-white/15 hover:border-brand-yellow-500 shadow-sm p-2.5 group cursor-pointer"
                    title="Instagram @enviosdosruedas"
                    aria-label="Instagram Oficial"
                  >
                    <FaInstagram className="h-5 w-5" />
                  </Link>
                </motion.div>

                {/* Facebook — spring bounce */}
                <motion.div
                  whileHover={prefersReducedMotion ? {} : SOCIAL_HOVER}
                  transition={SOCIAL_SPRING}
                  className="inline-block"
                >
                  <Link
                    href="/nosotros/nuestras-redes"
                    className="h-10 w-10 rounded-xl bg-white/10 hover:bg-brand-yellow-500 text-white hover:text-brand-blue-900 flex items-center justify-center transition-colors duration-200 border border-white/15 hover:border-brand-yellow-500 shadow-sm p-2.5 group cursor-pointer"
                    title="Facebook Envíos DosRuedas"
                    aria-label="Facebook Oficial"
                  >
                    <FaFacebook className="h-5 w-5" />
                  </Link>
                </motion.div>

                {/* WhatsApp — spring bounce */}
                <motion.div
                  whileHover={prefersReducedMotion ? {} : SOCIAL_HOVER}
                  transition={SOCIAL_SPRING}
                  className="inline-block"
                >
                  <a
                    href="https://wa.me/542236602699"
                    target="_blank"
                    rel="noopener noreferrer"
                    className="h-10 w-10 rounded-xl bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 flex items-center justify-center transition-colors duration-200 border border-brand-yellow-500 hover:border-brand-yellow-400 shadow-accent-sm hover:shadow-cta-glow p-2.5 group cursor-pointer"
                    title="WhatsApp Directo"
                    aria-label="WhatsApp Directo"
                  >
                    <FaWhatsapp className="h-5 w-5" />
                  </a>
                </motion.div>

                <div className="flex items-center gap-2 px-3.5 py-2 rounded-xl bg-white/10 border border-white/15 text-xs text-white font-mono shadow-inner">
                  <ShieldCheck className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                  <span>Centro de Depósito y Logística Local · Friuli 1972</span>
                </div>
              </div>
            </div>
          </motion.div>

          {/* COLUMN 2: Services & Tools */}
          <motion.div
            variants={prefersReducedMotion ? {} : FOOTER_COL}
            className="lg:col-span-4 space-y-5"
          >
            <h4 className="font-subheading text-lg tracking-wider text-brand-yellow-500 uppercase border-b border-white/10 pb-2 font-bold flex items-center gap-2">
              <span>Servicios y Cotizadores</span>
            </h4>
            <div className="grid grid-cols-1 sm:grid-cols-2 gap-x-6 gap-y-4">
              {/* Grupo Cotizadores */}
              <div>
                <p className="text-2xs font-bold text-brand-blue-50/70 uppercase tracking-widest font-subheading mb-2.5">
                  Cotizador online
                </p>
                <ul className="space-y-2.5 text-sm font-sans">
                  <li>
                    <Link
                      href="/cotizar"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center justify-between group transition-all duration-200 hover:translate-x-1"
                    >
                      <div className="flex items-center gap-2.5">
                        <Zap className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                        <span>Cotizá Express o LowCost</span>
                      </div>
                      <ArrowUpRight className="h-3.5 w-3.5 opacity-0 group-hover:opacity-100 transition-opacity text-brand-yellow-500" />
                    </Link>
                  </li>
                </ul>
              </div>

              {/* Grupo Servicios y Planes */}
              <div>
                <p className="text-2xs font-bold text-brand-blue-50/70 uppercase tracking-widest font-subheading mb-2.5">
                  Servicios y planes
                </p>
                <ul className="space-y-2.5 text-sm font-sans">
                  <li>
                    <Link
                      href="/servicios/envios-express"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Zap className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>Envíos Express</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios/envios-lowcost"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <TrendingDown className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>Envíos LowCost</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios/enviosflex"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Clock className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>Mercado Envíos Flex</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios/empresas-cuenta-corriente"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Building2 className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>Cuenta Corriente Flexible</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios#ecommerce-24hs"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Package className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>E-commerce 24HS</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios/deposito-fulfillment"
                      className="text-brand-blue-50 hover:text-brand-yellow-500 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1"
                    >
                      <Store className="h-4 w-4 text-brand-yellow-500 shrink-0" />
                      <span>E-commerce Same Day</span>
                    </Link>
                  </li>
                  <li>
                    <Link
                      href="/servicios"
                      className="text-brand-yellow-500 hover:text-brand-yellow-400 flex items-center gap-2.5 transition-all duration-200 hover:translate-x-1 font-bold"
                    >
                      <Layers className="h-4 w-4 shrink-0" />
                      <span>Ver todos los servicios</span>
                    </Link>
                  </li>
                </ul>
              </div>
            </div>
          </motion.div>

          {/* COLUMN 3: Contact & Hub Operations Info (4 Cols) */}
          <motion.div
            variants={prefersReducedMotion ? {} : FOOTER_COL}
            className="lg:col-span-4 space-y-5"
          >
            <h4 className="font-subheading text-lg tracking-wider text-brand-yellow-500 uppercase border-b border-white/10 pb-2 font-bold">
              Base de Operaciones MDQ
            </h4>

            <div className="space-y-3.5 text-xs text-brand-blue-50 font-sans">
              <div className="flex gap-3 items-start bg-brand-blue/80 p-3 rounded-xl border border-white/15">
                <div className="p-2 bg-white/10 rounded-lg shrink-0 text-brand-yellow-500">
                  <MapPin className="h-4 w-4" />
                </div>
                <div>
                  <p className="font-bold text-white uppercase font-subheading tracking-wider">Centro de Distribución</p>
                  <p className="font-sans text-[13px] text-brand-blue-50 mt-0.5">Friuli 1972, Mar del Plata</p>
                </div>
              </div>

              <div className="flex gap-3 items-start bg-brand-blue/80 p-3 rounded-xl border border-white/15">
                <div className="p-2 bg-white/10 rounded-lg shrink-0 text-brand-yellow-500">
                  <Phone className="h-4 w-4" />
                </div>
                <div>
                  <p className="font-bold text-white uppercase font-subheading tracking-wider">Línea Directa y WhatsApp</p>
                  <a href="tel:+542236602699" className="font-mono text-[13px] font-bold text-brand-yellow-500 hover:underline block mt-0.5">
                    +54 223 660-2699
                  </a>
                </div>
              </div>

              <div className="flex gap-3 items-start bg-brand-blue/80 p-3 rounded-xl border border-white/15">
                <div className="p-2 bg-white/10 rounded-lg shrink-0 text-brand-yellow-500">
                  <Mail className="h-4 w-4" />
                </div>
                <div>
                  <p className="font-bold text-white uppercase font-subheading tracking-wider">Atención Comercial</p>
                  <a href="mailto:matiascejas@enviosdosruedas.com" className="font-sans text-[12px] text-brand-blue-50 hover:text-brand-yellow-500 transition-colors block mt-0.5 break-all">
                    matiascejas@enviosdosruedas.com
                  </a>
                </div>
              </div>

              <div className="flex gap-3 items-start bg-brand-blue/80 p-3 rounded-xl border border-white/15">
                <div className="p-2 bg-white/10 rounded-lg shrink-0 text-brand-yellow-500">
                  <Clock className="h-4 w-4" />
                </div>
                <div className="space-y-1">
                  <p className="font-bold text-white uppercase font-subheading tracking-wider">Horarios de Despacho (Base Central)</p>
                  <div className="text-[12px] font-sans text-brand-blue-50 space-y-0.5">
                    <div className="flex justify-between items-center gap-4">
                      <span>Lunes a Viernes:</span>
                      <span className="font-mono font-bold text-brand-yellow-500">09:00 - 18:00 hs</span>
                    </div>
                    <div className="flex justify-between items-center gap-4">
                      <span>Sábados:</span>
                      <span className="font-mono font-bold text-brand-yellow-500">10:00 - 15:00 hs</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </motion.div>

        </motion.div>

        {/* Separator */}
        <div className="border-t border-white/10 my-10 relative">
          {/* Scroll to Top — continuous float loop */}
          <motion.button
            onClick={scrollToTop}
            className="absolute -top-5 right-4 sm:right-6 bg-brand-yellow-500 hover:bg-brand-yellow-400 text-brand-blue-900 p-2.5 rounded-full shadow-accent-md hover:shadow-cta-glow transition-colors flex items-center justify-center border-2 border-brand-yellow-500 cursor-pointer"
            title="Volver al inicio"
            aria-label="Volver arriba"
            /* Idle float loop */
            animate={prefersReducedMotion ? {} : { y: [0, -5, 0] }}
            transition={
              prefersReducedMotion
                ? {}
                : { duration: 2, ease: 'easeInOut', repeat: Infinity, repeatType: 'loop' }
            }
            /* Tap feedback */
            whileTap={{ scale: 0.92 }}
            whileHover={prefersReducedMotion ? {} : { scale: 1.1, y: -7 }}
          >
            <ArrowUp className="h-4 w-4 font-bold" />
          </motion.button>
        </div>

        {/* BOTTOM SECTION: Legal & Copyright */}
        <div className="flex flex-col md:flex-row justify-between items-center gap-6 text-xs text-brand-blue-50 font-sans">
          <div className="flex flex-wrap justify-center md:justify-start items-center gap-4 sm:gap-6">
            <p className="font-medium text-white">© 2026 Envíos DosRuedas · Mar del Plata, Argentina.</p>
            <Link href="/servicios" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Servicios
            </Link>
            <Link href="/cobertura" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Cobertura
            </Link>
            <Link href="/guias/envios-flex-mar-del-plata" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Guía MercadoLibre Flex
            </Link>
            <Link href="/nosotros/sobre-nosotros" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Sobre Nosotros
            </Link>
            <Link href="/nosotros/preguntas-frecuentes" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Preguntas Frecuentes
            </Link>
            <Link href="/nosotros/nuestras-redes" className="hover:text-brand-yellow-500 transition-colors text-brand-blue-50">
              Nuestras Redes
            </Link>
          </div>
          <div className="flex flex-wrap justify-center gap-6 shrink-0 text-brand-blue-50">
            <Link href="/terminos-y-condiciones" className="hover:text-brand-yellow-500 transition-colors">
              Términos y Condiciones
            </Link>
            <Link href="/politica-de-privacidad" className="hover:text-brand-yellow-500 transition-colors">
              Política de Privacidad
            </Link>
          </div>
        </div>

      </div>
    </footer>
  );
}

```

### Pricing Constants & Tiers (src/lib/pricing.ts) (`src/lib/pricing.ts`)

```typescript
/**
 * Funciones puras de cálculo de precios para los servicios de Envíos DosRuedas.
 * Al ser puras (sin dependencias de React ni I/O), son completamente testeables.
 */

export interface PriceRangeProp {
  id: number;
  serviceType: string;
  distanciaMinKm: number;
  distanciaMaxKm: number;
  precioRango: number;
  descripcion: string;
}

/** Tramo de tarifa fija: se aplica a distancias mayores que `minKm` y hasta `maxKm` inclusive. */
export interface PriceTier {
  minKm: number;
  maxKm: number;
  price: number;
}

/**
 * Tarifas oficiales 2026 (docs/contexto/precios.md). Son el fallback cuando `PriceRange`
 * está vacía y la única fuente para mostrar tarifas en la UI: no copiar estos valores a mano.
 */
export const EXPRESS_TIERS: readonly PriceTier[] = [
  { minKm: 0, maxKm: 3, price: 3700 },
  { minKm: 3, maxKm: 5, price: 4600 },
  { minKm: 5, maxKm: 7, price: 6100 },
  { minKm: 7, maxKm: 10, price: 8200 },
];
export const EXPRESS_PRICE_PER_KM = 1000;

export const LOW_COST_TIERS: readonly PriceTier[] = [
  { minKm: 0, maxKm: 3, price: 3000 },
  { minKm: 3, maxKm: 5, price: 4000 },
  { minKm: 5, maxKm: 7, price: 5300 },
  { minKm: 7, maxKm: 10, price: 7000 },
];
export const LOW_COST_PRICE_PER_KM = 700;

/**
 * Calcula precio: tramo fijo si distanceKm <= maxKm, sino distanceKm × pricePerKm (lineal).
 * NO usa Math.ceil — corrección dueño octubre 2026: precio por km lineal.
 * Redondea al entero más cercano para evitar problemas de punto flotante.
 */
function fallbackPrice(distanceKm: number, tiers: readonly PriceTier[], pricePerKm: number): number {
  const tier = tiers.find((t) => distanceKm <= t.maxKm);
  return tier ? tier.price : Math.round(distanceKm * pricePerKm);
}

/**
 * Calcula el precio del servicio Express para una distancia dada.
 *
 * Lógica de rangos (según BD):
 *   0–3 km  → $3.700
 *   3–5 km  → $4.600
 *   5–7 km  → $6.100
 *   7–10 km → $8.200
 *   +10 km  → distanceKm × $1.000  (km total × precio por km, LINEAL)
 *
 * @param distanceKm  Distancia en kilómetros (puede tener decimales).
 * @param priceRanges Rangos de precios obtenidos desde la base de datos.
 * @returns El precio en ARS o `'consultar'` si supera los 20 km.
 */
export function calculateExpressPrice(
  distanceKm: number,
  priceRanges: PriceRangeProp[]
): number | 'consultar' {
  if (distanceKm > 20) return 'consultar';

  const expressRanges = priceRanges.filter((r) => r.serviceType === 'EXPRESS');

  if (expressRanges.length > 0) {
    const matchingRange = expressRanges.find(
      (r) => (r.distanciaMinKm === 0 ? distanceKm >= r.distanciaMinKm : distanceKm > r.distanciaMinKm) && distanceKm <= r.distanciaMaxKm
    );

    if (matchingRange) {
      if (matchingRange.distanciaMaxKm === 9999) {
        // Rango extendido (+10 km): cantidad total de km × precio unitario por km (LINEAL)
        return Math.round(distanceKm * matchingRange.precioRango);
      }
      return matchingRange.precioRango;
    }
  } else {
    // Fallback cuando la tabla de precios de la BD está vacía — misma lógica de rangos
    return fallbackPrice(distanceKm, EXPRESS_TIERS, EXPRESS_PRICE_PER_KM);
  }

  return 'consultar';
}

/**
 * Calcula el precio del servicio LowCost para una distancia dada.
 *
 * Lógica de rangos (según BD):
 *   0–3 km  → $3.000
 *   3–5 km  → $4.000
 *   5–7 km  → $5.300
 *   7–10 km → $7.000
 *   +10 km  → distanceKm × $700  (km total × precio por km, LINEAL)
 *
 * @param distanceKm  Distancia en kilómetros (puede tener decimales).
 * @param priceRanges Rangos de precios obtenidos desde la base de datos.
 * @returns El precio en ARS o `'consultar'` si supera los 20 km.
 */
export function calculateLowCostPrice(
  distanceKm: number,
  priceRanges: PriceRangeProp[]
): number | 'consultar' {
  if (distanceKm > 20) return 'consultar';

  const lowCostRanges = priceRanges.filter((r) => r.serviceType === 'LOW_COST');

  if (lowCostRanges.length > 0) {
    const matchingRange = lowCostRanges.find(
      (r) => (r.distanciaMinKm === 0 ? distanceKm >= r.distanciaMinKm : distanceKm > r.distanciaMinKm) && distanceKm <= r.distanciaMaxKm
    );

    if (matchingRange) {
      if (matchingRange.distanciaMaxKm === 9999) {
        // Rango extendido (+10 km): cantidad total de km × precio unitario por km (LINEAL)
        return Math.round(distanceKm * matchingRange.precioRango);
      }
      return matchingRange.precioRango;
    }
  } else {
    // Fallback cuando la tabla de precios de la BD está vacía — misma lógica de rangos
    return fallbackPrice(distanceKm, LOW_COST_TIERS, LOW_COST_PRICE_PER_KM);
  }

  return 'consultar';
}

```

### Business Promises & Service Constants (src/lib/promises.ts) (`src/lib/promises.ts`)

```typescript
/**
 * Constantes únicas de promesas de servicio y umbrales operativos (BL-03).
 * Fuente de verdad unificada para cotizadores, páginas informativas, JSON-LD y llms.txt.
 *
 * Nota: Si se modifican estas promesas, recordar actualizar sincronizadamente también
 * public/llms.txt y public/llms-full.txt.
 *
 * Contexto del dueño (definiciones verbatim de servicio, recargos, protocolos y lo que
 * niega explícitamente): docs/knowledge_base/00-negocio/servicios.md y voz-y-lineas-rojas.md
 */

// Ventana de entrega Express.
// Cambio 2026-09-29 (decisión del dueño, relevamiento con Matías Cejas): la promesa de
// "60 a 90 min" se retiró por inexacta. Express coordina hoy una franja horaria acotada
// a elección del cliente, con 2 hs de anticipación mínima.
//
// Contrato de las dos formas, porque se interpolan en oraciones distintas:
//   EXPRESS_WINDOW       → forma larga. SIEMPRE después de "en" o "Entrega en":
//                          "Entrega en franja horaria de 3 hs".
//   EXPRESS_WINDOW_SHORT → forma compacta, para chips, tablas y rótulos sueltos:
//                          "Franja de 3 hs". NUNCA dentro de una oración con "en",
//                          porque "en 3 hs" se leería como duración de la entrega.
export const EXPRESS_WINDOW = 'franja horaria de 3 hs';
export const EXPRESS_WINDOW_SHORT = 'Franja de 3 hs';

// Anticipación mínima para coordinar una franja de Express.
export const EXPRESS_LEAD_TIME = '2 hs de anticipación';

// Corte Express: pedido hasta esta hora para entregar en el día. El último rango
// posible es 17 a 19 hs (entrevista 2026-09-28 §1.1).
export const EXPRESS_CUTOFF_TIME = '15:00 hs';

// Ventanas operativas LowCost
export const LOWCOST_CUTOFF_TIME = '13:00 hs';
export const LOWCOST_DELIVERY_DEADLINE = '19:00 hs';

// Mercado Envíos Flex
export const FLEX_CUTOFF_TIME = '15:00 hs';
export const FLEX_DELIVERY_DEADLINE = '20:00 hs';

// Tarifas fijas de los niveles Flex. Fuera de `PriceRange`: son precio cerrado
// por nivel, no un rango por distancia. El Nivel 1 no tiene cifra propia —cobra
// la tabla LowCost por zona (ver `LOW_COST_TIERS` en `pricing.ts`).
export const FLEX_NIVEL_2_PRICE = 6500; // Tope fijo en Z4 y Z5
export const FLEX_NIVEL_3_PRICE = 4500; // Tarifa plana a todo Mar del Plata

// Recargo por lluvia. El dueño (entrevista 2026-09-28) define un rango según el
// servicio: 50 % para Express y LowCost, 30 % en todos los demás. Esta constante
// modela SOLO el caso de 30 %, que es el único que hoy se muestra en el sitio.
// Antes de usar este valor para Express o LowCost, agregar el desglose por servicio.
// Ver docs/knowledge_base/00-negocio/tarifas.md §7.
export const RAIN_SURCHARGE_PERCENT = 30;

// Recargo por lluvia para Express y LowCost (el caso de 50 % del rango del dueño).
export const RAIN_SURCHARGE_PERCENT_EXPRESS_LOWCOST = 50;

// Recargos operativos de Express y LowCost (entrevista 2026-09-28 §3). Se informan
// en el cotizador pero no entran en el cálculo automático: dependen de lo que pase
// en el viaje (lluvia, espera, paradas, destinatario ausente).
export const WAIT_TOLERANCE_MIN = 10; // Espera en puerta sin cargo
export const WAIT_CHARGE_ARS = 2200; // Por cada bloque de espera, desde el minuto 11 (corrección dueño oct 2026)
export const WAIT_CHARGE_BLOCK_MIN = 10;
export const EXTRA_STOP_SURCHARGE_PERCENT = 50; // Por parada intermedia sobre la ruta
export const EXTRA_STOP_MAX_DETOUR_KM = 2; // Más desvío que esto es un envío aparte
export const RETRY_CHARGE_PERCENT = 100; // Segunda visita por destinatario ausente

// Periferia: destinos fuera de la urbana de Mar del Plata (Batán, Sierra de los
// Padres…). NO es el excedente de 10 a 20 km de `pricing.ts` ($1.000 / $700 por km):
// es otra tarifa, por km de ruta, que se cotiza aparte. Ver entrevista §3.1.
export const PERIPHERY_PRICE_PER_KM = 1000;
// Bulto extra: más de 5 kg o 40 × 40 × 30 cm. Corrección dueño octubre 2026: desde $1800.
export const BULK_EXTRA_FROM_ARS = 1800;

// Umbrales de distancia y límites físicos
export const CONSULT_THRESHOLD_KM = 20; // Hasta 20 km cálculo automático; > 20 km "A consultar"

// Capacidad por bulto. UN umbral, dos formas de expresarlo:
//   STANDARD_WEIGHT_KG            → lo que entra sin recargo. Es el único número de
//                                   peso que va al copy y a las tarjetas de servicio.
//   STANDARD_BULLET_DIMENSIONS_CM → el mismo umbral en volumen.
//
// Sobrepasado el umbral, el bulto se coordina aparte y entra un recargo desde
// `BULK_EXTRA_FROM_ARS`, cuyo monto final depende del servicio. No entra en el
// cálculo automático del cotizador.
//
// SIN TECHO NUMÉRICO PUBLICADO, y es deliberado (decisión del dueño 2026-09-30).
// Existió una constante `MAX_WEIGHT_KG = 15` que ningún fuente del dueño respalda:
// el 15 kg venía solo del `.docx`, siempre como pregunta sin respuesta registrada
// o como aserción del propio `.docx` — la misma clase de número viejo que el
// dueño ya corrigió ahí ("60-90 min: ESTO ES FALSO"). Lo que el dueño sí
// respondió, textual, fue "todo lo que pueda ser llevado en moto" (CSV pregunta
// 4), sin cifra. Publicar un techo inventado además rompía el recargo por bulto
// extra: si el máximo fuera 5 kg, "más de 5 kg suma $1.800" sería imposible.
// Constante eliminada; el guard de `src/lib/copy-guard.test.ts` la bloquea.
export const STANDARD_WEIGHT_KG = 5;
export const STANDARD_BULLET_DIMENSIONS_CM = '40 × 40 × 30 cm';

// Condiciones comerciales Depósito & Fulfillment (servicio para empresas)
// No figuran en la tabla `PriceRange` ni en docs/contexto/precios.md: son tarifas
// cerradas definidas por el dueño. El 20 % de DropOFF quedó confirmado en el relevamiento
// del 2026-09-29; SAME_DAY_FIXED_PRICE se suma ese mismo día.
export const DROPOFF_DISCOUNT_PERCENT = 20; // Descuento por traer envíos listos al depósito
export const CONTRAREEMBOLSO_COMMISSION_PERCENT = 0; // Sin extra ni comisión por cobro en entrega

// Tarifa fija del plan E-Commerce Same Day para toda la ciudad. Fuera de `PriceRange`
// a propósito: es un precio cerrado por servicio, no un rango por distancia.
export const SAME_DAY_FIXED_PRICE = 6000;

// Tarifa fija E-Commerce 24HS (Next Day) — Confirmada por Matías 2026-09-29.
// Recolección gratis desde 10 envíos. DropOFF -20% solo en este servicio.
export const ECOMMERCE_24HS_PRICE = 3800;

/** Envíos/mes desde los cuales el retiro es gratis. */
export const ECOMMERCE_24HS_FREE_PICKUP_THRESHOLD = 10;

/**
 * Escala de planes E-Commerce 24HS. Vivían como literales dentro de
 * `Ecommerce24HSPricing.tsx`; se movieron acá para que haya una sola fuente,
 * como manda AGENTS.md.
 *
 * Procedencia: `Inicial` es `ECOMMERCE_24HS_PRICE`, confirmado de palabra por el
 * dueño el 2026-09-29. `Pro`, `Elite` y `Partner` salen de la escala que el
 * sitio ya publica; no hay confirmación verbal registrada para esos tres.
 * Si el dueño ajusta la escala, se corrige acá y en ningún otro lado.
 */
export const ECOMMERCE_24HS_PLANS = [
  { name: 'Inicial', fromEnvos: 1, toEnvios: 199, price: ECOMMERCE_24HS_PRICE, featured: false },
  { name: 'Pro', fromEnvos: 200, toEnvios: 1199, price: 3500, featured: true },
  { name: 'Elite', fromEnvos: 1200, toEnvios: 1999, price: 3200, featured: false },
  { name: 'Partner', fromEnvos: 2000, toEnvios: null, price: 3000, featured: false },
] as const;

/**
 * Planes de la landing de Emprendedores. Tarifas cerradas por plan, fuera de
 * `PriceRange`. El Plan Inicial DropOFF ya viene con el -20% aplicado sobre la
 * tarifa plana; el Plan PyME Corporativo no tiene cifra: se cotiza.
 */
export const EMPRENDEDORES_PLANS = [
  {
    name: 'Plan Inicial DropOFF',
    distance: 'Por envío en MDQ',
    price: 2400, // Tarifa base del Plan DropOFF. La consume también `DropoffCalculator`.
    period: '/ envío',
    tag: `DropOFF -${DROPOFF_DISCOUNT_PERCENT}%`,
    note: 'Traés tus paquetes listos a Friuli 1972 y el descuento se aplica solo.',
    featured: false,
  },
  {
    name: 'Plan E-Commerce 3PL',
    distance: 'Stock gratis',
    price: 3000,
    period: '/ envío + stock gratis',
    tag: 'Con depósito',
    note: 'Stock gratis en Friuli 1972 + picking QR + Same Day.',
    featured: true,
  },
  {
    name: 'Plan PyME Corporativo',
    distance: 'Volumen > 10 envíos/día',
    price: null,
    period: '',
    tag: 'Cuenta corriente',
    note: 'Para empresas con envíos diarios recurrentes. La tarifa se cotiza.',
    featured: false,
  },
] as const;

// Reglas de 2da visita / reintento por servicio (corrección dueño octubre 2026)
export const RETRY_RULES = {
  EXPRESS: { type: 'NEW_TRIP', description: 'Se cobra como viaje nuevo' },
  LOW_COST: { type: 'NEW_TRIP', description: 'Se cobra como viaje nuevo' },
  FLEX_NIVEL_1: { type: 'PERCENT', value: 50, description: '50% en todas las zonas' },
  FLEX_NIVEL_2: { type: 'ZONE_BASED', z1: 0, z2_to_z5: 50, description: 'Z1 gratis, Z2-Z5 50%' },
  FLEX_NIVEL_3: { type: 'FREE', description: '100% bonificada todas zonas' },
  DEPOSITO_3PL: { type: 'FREE', description: '100% bonificada' },
  ECOMMERCE_24HS: { type: 'FREE', description: '100% bonificada' },
  CUENTA_CORRIENTE: { type: 'PERCENT', value: 50, description: '50% del valor original' },
} as const;

// Horarios de atención oficiales en base central Friuli 1972 (Decisión 5 aprobada)
export const OPERATING_HOURS = {
  weekdays: '09:00 a 18:00 hs',
  saturdays: '10:00 a 15:00 hs',
  sundays: 'Cerrado',
} as const;

// Canales de contacto oficiales unificados (BL-19)
export const CONTACT_EMAIL = 'matiascejas@enviosdosruedas.com';
export const SUPPORT_PHONE = '+54 223 660-2699';

```

