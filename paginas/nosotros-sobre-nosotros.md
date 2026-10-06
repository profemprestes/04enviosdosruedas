# Documentación Completa y Código Autocontenido: Sobre Nosotros e Historia

> **Ruta URL:** `/nosotros/sobre-nosotros`  
> **Archivo de Página:** `src/app/nosotros/sobre-nosotros/page.tsx`  
> **Nota de Portabilidad:** Este documento incluye todo el código fuente de la página, sus componentes específicos, la estructura compartida del Layout (Header, Footer, Nav, CSS) y las constantes de negocio para permitir la generación de mockups HTML independientes sin depender del directorio `@src`.

---

## 1. Código Fuente de la Página (`src/app/nosotros/sobre-nosotros/page.tsx`)

```tsx
import React from 'react';
import { Metadata } from 'next';
import AboutHero from '@/components/nosotros/sobre-nosotros/AboutHero';
import AboutAdvantages from '@/components/nosotros/sobre-nosotros/AboutAdvantages';
import AboutValues from '@/components/nosotros/sobre-nosotros/AboutValues';
import AboutTimeline from '@/components/nosotros/sobre-nosotros/AboutTimeline';
import AboutTeam from '@/components/nosotros/sobre-nosotros/AboutTeam';
import AboutMissionVision from '@/components/nosotros/sobre-nosotros/AboutMissionVision';

const baseUrl = 'https://www.enviosdosruedas.com';

export const metadata: Metadata = {
  title: 'Sobre Nosotros y Trayectoria',
  description:
    'Conocé la historia, valores y equipo detrás de Envíos DosRuedas. Más de 7 años de trayectoria en logística urbana, cadetería y última milla e-commerce en Mar del Plata.',
  alternates: {
    canonical: `${baseUrl}/nosotros/sobre-nosotros`,
  },
  openGraph: {
    title: 'Sobre Nosotros y Trayectoria | Envíos DosRuedas',
    description:
      'Más de 7 años de trayectoria transformando la logística urbana y la última milla en Mar del Plata con flota propia.',
    url: `${baseUrl}/nosotros/sobre-nosotros`,
    type: 'website',
    locale: 'es_AR',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'Sobre Nosotros y Trayectoria | Envíos DosRuedas',
    description: 'Más de 7 años de trayectoria transformando la logística urbana y la última milla en Mar del Plata con flota propia.',
    images: [`${baseUrl}/og-image.jpg`],
    creator: '@enviosdosruedas',
  },
};

const jsonLdSchema = {
  '@context': 'https://schema.org',
  '@type': 'AboutPage',
  name: 'Sobre Nosotros - Envíos DosRuedas',
  description:
    'Historia, valores y equipo de Envíos DosRuedas en Mar del Plata. Más de 7 años de trayectoria en logística urbana y última milla.',
  url: `${baseUrl}/nosotros/sobre-nosotros`,
  mainEntity: {
    '@type': 'LocalBusiness',
    '@id': `${baseUrl}#localbusiness`,
    name: 'Envíos DosRuedas',
    description:
      'Somos tu aliado estratégico en logística urbana y mensajería de última milla. Con más de 7 años de trayectoria en Mar del Plata, transformamos el despacho de tus productos en un motor de crecimiento para emprendedores, PyMEs y comercios locales.',
    telephone: '+54-223-660-2699',
    email: 'matiascejas@enviosdosruedas.com',
    address: {
      '@type': 'PostalAddress',
      streetAddress: 'Friuli 1972',
      addressLocality: 'Mar del Plata',
      addressRegion: 'Buenos Aires',
      postalCode: '7600',
      addressCountry: 'AR',
    },
    numberOfEmployees: {
      '@type': 'QuantitativeValue',
      minValue: 20,
      maxValue: 50,
    },
  },
};

export default function SobreNosotrosPage() {
  return (
    <main className="min-h-dvh bg-brand-white-50 text-brand-ink relative overflow-hidden">
      <script
        type="application/ld+json"
        dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLdSchema) }}
      />

      {/* 3D Ambient floating glow-orbs */}
      <div className="absolute top-[15%] left-[-10%] w-[40vw] h-[40vw] bg-brand-blue-500/5 rounded-full blur-[130px] pointer-events-none" />
      <div className="absolute top-[50%] right-[-10%] w-[35vw] h-[35vw] bg-brand-yellow-500/5 rounded-full blur-[110px] pointer-events-none" />
      <div className="absolute bottom-[10%] left-[5%] w-[45vw] h-[45vw] bg-brand-blue-500/5 rounded-full blur-[130px] pointer-events-none" />

      {/* Hero Header & Identidad */}
      <div className="relative z-10">
        <AboutHero />
      </div>

      {/* Ventajas Territoriales */}
      <div className="relative z-10">
        <AboutAdvantages />
      </div>

      {/* Valores Operativos */}
      <div className="relative z-10">
        <AboutValues />
      </div>

      {/* Línea de Tiempo & Evolución Histórica */}
      <div className="relative z-10">
        <AboutTimeline />
      </div>

      {/* Equipo & Fuerza Operativa */}
      <div className="relative z-10">
        <AboutTeam />
      </div>

      {/* Misión, Visión & Cierre */}
      <div className="relative z-10 font-sans">
        <AboutMissionVision />
      </div>
    </main>
  );
}

```

---

## 2. Componentes Específicos Importados por esta Página

### Componente: `src/components/nosotros/sobre-nosotros/AboutHero.tsx`

```tsx
import { Bike, CalendarClock, MapPin, Navigation, ShieldCheck } from 'lucide-react';
import { FaWhatsapp } from 'react-icons/fa';
import { CTANestedPill } from '@/components/ui/CTANestedPill';
import { Knockout } from '@/components/ui/Knockout';
import Badge from '@/components/ui/Badge';
import HeroProceduralBackground from '@/components/ui/HeroProceduralBackground';
import {
  CONSULT_THRESHOLD_KM,
  LOWCOST_CUTOFF_TIME,
  LOWCOST_DELIVERY_DEADLINE,
  OPERATING_HOURS,
  SUPPORT_PHONE,
} from '@/lib/promises';

/**
 * El nodo: un único origen y siete direcciones.
 *
 * Lafan vive en un cuadrado `h-full aspect-square` anclado en la esquina
 * inferior izquierda de la banda, así un 1% de ancho mide lo mismo que un 1% de
 * alto: la geometría es isotrópica en cualquier breakpoint y ninguna cresta
 * puede exceder el alto de la banda. Sobre la línea de base, siete radios de
 * igual longitud (las puntas caen sobre un arco de cuarto de círculo) con un
 * punto amarillo en cada punta que se enciende en cascada.
 *
 * Los puntos usan `transform` para pulsar, así que van en un wrapper aparte del
 * que centra: la animación pisa cualquier `translate` de clase.
 */
const SPOKE_COUNT = 7;
const SPOKE_FIRST_ANGLE = 10;
const SPOKE_STEP = 10;
const SPOKE_LENGTH = 84; // % del lado del cuadrado = % del alto de la banda

const spokes = Array.from({ length: SPOKE_COUNT }, (_, i) => ({
  angle: SPOKE_FIRST_ANGLE + i * SPOKE_STEP,
  delay: i * 0.13,
}));

/**
 * Cifras de identidad. "+7 años" y "flota 100% propia" no viven en pricing.ts
 * porque no son tarifas: son claims institucionales ya publicados en el
 * metadata y el JSON-LD de esta misma página.
 */
const chips = [
  { icon: CalendarClock, value: '+7', label: 'Años en ruta' },
  { icon: Bike, value: '100%', label: 'Flota propia' },
  { icon: Navigation, value: `${CONSULT_THRESHOLD_KM} km`, label: 'Cálculo automático' },
];

/** Horarios de la base central, tal cual están en promesas.ts. */
const hours = [
  { label: 'Lun a Vie', value: OPERATING_HOURS.weekdays },
  { label: 'Sáb', value: OPERATING_HOURS.saturdays },
  { label: 'Dom', value: OPERATING_HOURS.sundays },
];

/**
 * Credenciales de la empresa, para la ficha lateral.
 *
 * "Operando +7 años" y "flota 100 % propia" son claims de identidad: ya están
 * en el metadata y el JSON-LD de esta página, así que repetirlos no inventa.
 * El corte y la última entrega sí salen de `promises.ts` — son los del servicio
 * LowCost, que es el que define la jornada.
 */
const credenciales = [
  { dt: 'Operando', dd: '+7 años' },
  { dt: 'Flota propia', dd: '100%' },
  { dt: 'Corte diario', dd: LOWCOST_CUTOFF_TIME },
  { dt: 'Última entrega', dd: LOWCOST_DELIVERY_DEADLINE },
];

/**
 * Hero Sobre Nosotros — concepto "el nodo".
 *
 * Esta página no vende un servicio: vende una empresa. La firma visual es una
 * base física con una sola dirección de origen y muchas de salida — el hub de
 * Friuli 1972 despacha en todas direcciones. Por eso el nodo va en el padding
 * inferior del hero y su alto es exactamente ese padding (`h-28 sm:h-36 lg:h-44`
 * = `pb-28 sm:pb-36 lg:pb-44`): no puede pisar texto ni card.
 *
 * La diferencia con las otras firmas: ninguna es radial. Home es un camino
 * abierto, Express una curva, LowCost un dial, Flex un riel con dos compuertas,
 * Emprendedores un estante. Acá no hay recorrido ni horario: hay origen.
 *
 * Todo el contenido sale de promesas.ts, salvo las dos cifras de identidad, que
 * son claims de la propia página.
 */
export default function AboutHero() {
  return (
    <section
      id="about-hero"
      aria-label="Sobre Envíos DosRuedas: base central en Friuli 1972, Mar del Plata, con flota propia y más de 7 años de trayectoria en logística urbana"
      className="relative isolate flex min-h-[90dvh] w-full flex-col overflow-hidden bg-brand-blue-500 text-white"
    >
      <HeroProceduralBackground variant="default" tone="blue" />

      {/* Palabra fantasma. Es lo único del hero que no es información: da la
          escala de un muro pintado y evita que el azul se lea como un bloque
          vacío. Va en z-0 y `aria-hidden` — el texto real es el H1. */}
      <span
        aria-hidden="true"
        className="pointer-events-none absolute bottom-[-8%] left-[-1%] z-0 whitespace-nowrap font-display text-[clamp(90px,17vw,230px)] uppercase leading-hero text-white/6"
      >
        Dos Ruedas
      </span>

      <div className="relative flex-1 flex items-center overflow-hidden">
        {/* Firma visual: el nodo. */}
        <div
          aria-hidden="true"
          className="absolute inset-x-0 bottom-0 h-28 sm:h-36 lg:h-44 overflow-hidden pointer-events-none"
        >
          {/* Línea de base: el piso desde el que sale todo. */}
          <div className="absolute inset-x-0 bottom-0 border-t border-dashed border-white/30" />

          <span className="absolute bottom-2 right-6 sm:right-8 font-mono text-2xs uppercase tracking-[0.18em] text-white/85 tabular-nums">
            Base central · Friuli 1972 · MDQ
          </span>

          {/* El cuadrado del nodo: isotrópico a propósito (ver nota arriba). */}
          <div className="absolute bottom-0 left-0 h-full aspect-square">
            {spokes.map(({ angle, delay }) => (
              <div
                key={angle}
                className="absolute bottom-0 left-0 h-px w-[84%] origin-left"
                style={{ transform: `rotate(${-angle}deg)` }}
              >
                <span className="block h-px w-full bg-white/40" />
                <span className="absolute right-0 top-0 -translate-y-1/2">
                  <span
                    className="block h-2 w-2 rounded-full bg-brand-yellow-500 motion-safe:animate-pulse"
                    style={{ animationDelay: `${delay}s` }}
                  />
                </span>
              </div>
            ))}

            {/* El nodo: un anillo que emite y el punto de la base. */}
            <span className="absolute bottom-0 left-0 h-0 w-0">
              <span className="absolute left-0 top-0 -translate-x-1/2 -translate-y-1/2">
                <span
                  className="block h-7 w-7 rounded-full border border-brand-yellow-500/60 motion-safe:animate-ping [animation-duration:3.6s]"
                />
              </span>
              <span className="absolute left-0 top-0 block h-2.5 w-2.5 -translate-x-1/2 -translate-y-1/2 rounded-full bg-brand-white-50" />
            </span>
          </div>
        </div>

        <div className="relative z-10 mx-auto w-full max-w-7xl px-6 lg:px-8 pt-14 sm:pt-20 lg:pt-24 pb-28 sm:pb-36 lg:pb-44">
          <div className="grid grid-cols-1 lg:grid-cols-12 gap-12 lg:gap-14 items-center">
            {/* LEFT 7 — copy + CTA. Nunca centrado en desktop. */}
            <div className="lg:col-span-7 space-y-6 sm:space-y-8 text-center lg:text-left">
              <Badge
                variant="outline"
                size="lg"
                className="-rotate-1 border-brand-yellow-500/60 text-brand-yellow-500"
                icon={<ShieldCheck className="h-4 w-4" aria-hidden="true" />}
              >
                Identidad · Mar del Plata
              </Badge>

              <h1 className="text-4xl sm:text-5xl lg:text-6xl xl:text-7xl font-display uppercase tracking-[-0.03em] leading-[0.92] text-white text-balance">
                <span className="block">Más que cadetería,</span>
                <Knockout>somos logística</Knockout>
                <span className="block">de confianza</span>
              </h1>

              <p className="text-base sm:text-lg font-sans text-white/85 max-w-[56ch] mx-auto lg:mx-0 leading-relaxed font-light">
                Una base física en Friuli 1972 y flota motorizada 100% propia. Conectamos
                tiendas online, PyMEs y emprendedores de todo Mar del Plata con soporte en
                tiempo real y cumplimiento estricto de horarios.
              </p>

              <div className="flex flex-col sm:flex-row items-center gap-4 sm:gap-6 justify-center lg:justify-start pt-1">
                <CTANestedPill
                  href="/contacto"
                  id="about-hero-cta-contacto"
                  variant="primary"
                  size="large"
                  className="focus-visible:ring-2 focus-visible:ring-brand-yellow-500 focus-visible:ring-offset-2 focus-visible:ring-offset-brand-blue-500"
                >
                  Trabajemos juntos
                </CTANestedPill>
                <a
                  href="https://wa.me/542236602699?text=Hola!%20Quiero%20conocer%20la%20operativa%20de%20DosRuedas"
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex min-h-11 items-center gap-2 font-subheading text-sm sm:text-base uppercase tracking-wider text-white underline decoration-brand-yellow-500 decoration-2 underline-offset-4 hover:text-brand-yellow-500 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-brand-yellow-500 focus-visible:ring-offset-2 focus-visible:ring-offset-brand-blue-500 rounded-md"
                >
                  <FaWhatsapp className="h-5 w-5 shrink-0" aria-hidden="true" />
                  Escribinos
                </a>
              </div>

              <ul className="grid grid-cols-3 gap-2.5 sm:gap-3 pt-3 max-w-xl mx-auto lg:mx-0">
                {chips.map((chip) => (
                  <li key={chip.label} className="p-3 rounded-xl bg-white/10 border border-white/20 text-center">
                    <chip.icon className="w-4 h-4 mx-auto text-brand-yellow-500" aria-hidden="true" />
                    <span className="block font-mono text-lg sm:text-2xl text-brand-yellow-500 tabular-nums mt-1.5">{chip.value}</span>
                    <span className="block font-subheading text-2xs sm:text-xs uppercase tracking-wider text-white mt-0.5">{chip.label}</span>
                  </li>
                ))}
              </ul>
            </div>

            {/* RIGHT 5 — ficha de la empresa: sello de la base + credenciales.
                El marco blanco hace de bisel y el panel azul interior repite el
                color del hero, así el bloque se apoya en la página en vez de
                flotar como un recorte. */}
            <div className="relative flex w-full flex-col items-center justify-center lg:col-span-5">
              <div className="w-full max-w-md rounded-[20px] border border-brand-blue-100 bg-white p-2.5 shadow-[0_25px_50px_-12px_rgba(9,80,246,0.18)]">
                <div className="flex flex-col gap-4 rounded-[14px] bg-brand-blue-500 p-5">
                  {/* Sello de la base. El ladeo de 1,5° es lo que lo hace leer
                      como sello y no como un encabezado más. */}
                  <div className="rotate-[-1.5deg] self-start rounded-xl border-2 border-brand-yellow-500 px-3.5 py-3">
                    <span className="block font-display text-3xl uppercase leading-none tracking-[-0.01em] text-brand-yellow-500">
                      Friuli 1972
                    </span>
                    <span className="mt-1 block font-mono text-xs font-medium leading-snug text-brand-blue-50">
                      Base central
                    </span>
                  </div>

                  <dl className="grid gap-2.5">
                    {credenciales.map(({ dt, dd }) => (
                      <div
                        key={dt}
                        className="flex items-baseline justify-between gap-3 border-t border-white/18 pt-2.5"
                      >
                        <dt className="font-subheading text-base uppercase tracking-[0.08em] text-brand-blue-50">
                          {dt}
                        </dt>
                        <dd className="font-mono text-xl font-bold tabular-nums text-white">
                          {dd}
                        </dd>
                      </div>
                    ))}
                  </dl>

                  <dl className="grid gap-1.5 border-t border-white/18 pt-3 font-mono text-xs tabular-nums text-brand-blue-50">
                    {hours.map((row) => (
                      <div key={row.label} className="flex items-baseline justify-between gap-3">
                        <dt className="font-subheading text-xs uppercase tracking-wider">
                          {row.label}
                        </dt>
                        <dd className="truncate text-right text-white">{row.value}</dd>
                      </div>
                    ))}
                  </dl>

                  <p className="flex items-center justify-between gap-3 border-t border-white/18 pt-3 font-mono text-xs tabular-nums text-brand-blue-50">
                    <span className="flex items-center gap-1.5 truncate">
                      <MapPin className="h-3.5 w-3.5 shrink-0" aria-hidden="true" />
                      Mar del Plata
                    </span>
                    <span className="shrink-0 text-white">{SUPPORT_PHONE}</span>
                  </p>
                </div>
              </div>
            </div>
          </div>
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

### Componente: `src/components/nosotros/sobre-nosotros/AboutAdvantages.tsx`

```tsx
'use client';

import React from 'react';
import { motion } from 'motion/react';
import { MessageSquare, ShieldCheck, Truck, Sparkles } from 'lucide-react';
import DoubleBezelCard from '@/components/ui/DoubleBezelCard';
import CTANestedPill from '@/components/ui/CTANestedPill';

export default function AboutAdvantages() {
  return (
    <section
      id="about-advantages"
      className="py-20 sm:py-24 bg-white relative overflow-hidden border-t border-brand-blue-100"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

        {/* Header Block */}
        <div className="text-center max-w-3xl mx-auto mb-16 space-y-3.5">
          <span className="px-4 py-1.5 bg-brand-yellow-500 text-brand-blue-900 rounded-full text-xs sm:text-sm font-subheading uppercase tracking-widest inline-block transform -rotate-1 shadow-glow-yellow">
            VENTAJAS TERRITORIALES
          </span>
          <h2 className="text-brand-blue-700 text-3xl sm:text-5xl lg:text-6xl font-display uppercase tracking-tight leading-[1.05]">
            POR QUÉ CONFIAR EN DOSRUEDAS
          </h2>
          <p className="text-brand-blue-700 font-sans text-sm sm:text-base max-w-2xl mx-auto leading-relaxed">
            Frente a aplicaciones automatizadas y plataformas impersonales, nosotros brindamos compromiso presencial, operadores locales y conocimiento metro a metro de Mar del Plata.
          </p>
        </div>

        {/* Asymmetric Bento Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8">

          {/* Card 1: Soporte Humano Directo (7 cols) */}
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="lg:col-span-7"
          >
            <DoubleBezelCard>
              <div className="space-y-4 flex flex-col justify-between h-full">
                <div className="space-y-4">
                  <div className="w-12 h-12 bg-brand-blue-50 text-brand-blue-700 rounded-2xl flex items-center justify-center border border-brand-blue-100">
                    <MessageSquare className="h-6 w-6 text-brand-blue-700" />
                  </div>
                  <h3 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-brand-blue-700 leading-tight">
                    Atención Humana y Directa
                  </h3>
                  <p className="text-sm sm:text-base text-brand-blue-700 leading-relaxed font-sans">
                    Damos la cara siempre. Cuando surge una duda o reprogramación, te comunicás directamente por WhatsApp con operadores en Mar del Plata que gestionan y resuelven en el acto.
                  </p>
                </div>
                <div className="pt-4 border-t border-brand-blue-100 flex items-center gap-2 text-xs font-subheading uppercase tracking-wider text-brand-blue-700">
                  <Sparkles className="h-4 w-4 text-brand-blue-700 fill-current" />
                  <span>COMUNICACIÓN DIRECTA VÍA WHATSAPP</span>
                </div>
              </div>
            </DoubleBezelCard>
          </motion.div>

          {/* Card 2: Flota Propia Coordinada (5 cols) */}
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: 0.1 }}
            className="lg:col-span-5"
          >
            <DoubleBezelCard>
              <div className="space-y-4 flex flex-col justify-between h-full">
                <div className="space-y-4">
                  <div className="w-12 h-12 bg-brand-yellow-500/20 text-brand-blue-700 rounded-2xl flex items-center justify-center border border-brand-yellow-500/40">
                    <Truck className="h-6 w-6 text-brand-blue-700" />
                  </div>
                  <h3 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-brand-blue-700 leading-tight">
                    Flota Propia Capacitada
                  </h3>
                  <p className="text-sm sm:text-base text-brand-blue-700 leading-relaxed font-sans">
                    No tercerizamos de forma descontrolada. Nuestro equipo de cadetes está uniformado, capacitado en manejo de paquetes frágiles y con base física en <strong>Friuli 1972</strong>.
                  </p>
                </div>
                <div className="pt-4 border-t border-brand-blue-100 flex items-center gap-2 text-xs font-subheading uppercase tracking-wider text-brand-blue-700">
                  <Sparkles className="h-4 w-4 text-brand-blue-700 fill-current animate-pulse" />
                  <span>COBERTURA TOTAL GENERAL PUEYRREDÓN</span>
                </div>
              </div>
            </DoubleBezelCard>
          </motion.div>

          {/* Card 3: Garantía de Puntualidad (12 cols full width) */}
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="lg:col-span-12"
          >
            <DoubleBezelCard>
              <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
                <div className="space-y-3 max-w-3xl">
                  <div className="flex items-center gap-3">
                    <div className="p-2.5 bg-brand-blue-50 text-brand-blue-700 rounded-xl">
                      <ShieldCheck className="h-6 w-6 text-brand-blue-700" />
                    </div>
                    <h3 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-brand-blue-700 leading-none">
                      Garantía Operativa Sin Excusas
                    </h3>
                  </div>
                  <p className="text-sm sm:text-base text-brand-blue-700 leading-relaxed font-sans">
                    Tu reputación comercial depende de la puntualidad de entrega. Si coordinamos un envío express en 2 horas o un ruteo programado, cumplimos la franja pactada sin desvíos.
                  </p>
                </div>
                <div className="shrink-0 flex items-center">
                  <CTANestedPill
                    href="/cotizar"
                    variant="primary"
                  >
                    Cotizar tu Envío
                  </CTANestedPill>
                </div>
              </div>
            </DoubleBezelCard>
          </motion.div>

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

### Componente: `src/components/nosotros/sobre-nosotros/AboutValues.tsx`

```tsx
'use client';

import React from 'react';
import { motion } from 'motion/react';
import { ShieldCheck, Handshake, Heart } from 'lucide-react';
import DoubleBezelCard from '@/components/ui/DoubleBezelCard';

export default function AboutValues() {
  const values = [
    {
      title: 'Transparencia Total',
      desc: 'Tarifas públicas por kilómetro exacto, con los recargos del viaje publicados. Lo que no sabés al cotizar no aparece después en la liquidación.',
      icon: Handshake,
    },
    {
      title: 'Cuidado del Paquete',
      desc: 'Tratamos cada paquete como si fuera nuestro. Mochilas reforzadas, cajas seguras y manipulación profesional de mercadería frágil.',
      icon: ShieldCheck,
      featured: true,
    },
    {
      title: 'Innovación Tecnológica',
      desc: 'Ruteo optimizado en tiempo real, trazabilidad GPS instantánea y avisos automáticos para tus clientes en Mar del Plata.',
      icon: Heart,
    },
  ];

  return (
    <section 
      id="about-values" 
      className="py-20 sm:py-24 bg-brand-blue text-white relative z-10 overflow-hidden border-t border-white/10"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* Header Block */}
        <div className="text-left max-w-2xl mb-16 space-y-3.5">
          <span className="px-4 py-1.5 bg-brand-yellow text-brand-blue rounded-full text-xs sm:text-sm font-subheading uppercase tracking-widest inline-block font-bold transform -rotate-1 shadow-glow-yellow">
            FILOSOFÍA OPERATIVA
          </span>
          <h2 className="text-white text-3xl sm:text-5xl lg:text-6xl font-display uppercase tracking-tight leading-[1.05]">
            NUESTROS VALORES
          </h2>
          <p className="text-brand-blue-50 font-sans text-base sm:text-lg max-w-prose leading-relaxed">
            Los pilares innegociables que sostienen nuestra operativa diaria en cada barrio de Mar del Plata.
          </p>
        </div>

        {/* Values Asymmetrical Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6">
          
          {/* Featured Value (Cuidado Extremo) - 7 cols */}
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="lg:col-span-7"
          >
            <DoubleBezelCard>
              <div className="flex flex-col gap-6 h-full justify-between">
                <div className="w-14 h-14 bg-brand-blue-50 text-brand-blue rounded-2xl flex items-center justify-center border border-brand-blue-100">
                  <ShieldCheck className="h-7 w-7 text-brand-blue" />
                </div>

                <div className="space-y-3">
                  <span className="text-xs font-subheading uppercase tracking-wider text-brand-blue font-bold bg-brand-yellow px-3 py-1 rounded-full w-fit transform -rotate-1 inline-block">
                    Pilar de Confianza
                  </span>
                  <h3 className="text-3xl sm:text-4xl font-display uppercase tracking-tight text-brand-ink leading-tight">
                    Cuidado del Paquete
                  </h3>
                  <p className="text-brand-ink font-sans leading-relaxed text-sm sm:text-base max-w-prose">
                    Manipulación profesional de paquetería e-commerce, indumentaria, tecnología y repuestos. Cada envío viaja seguro y protegido de las inclemencias del clima marplatense.
                  </p>
                </div>
              </div>
            </DoubleBezelCard>
          </motion.div>

          {/* Secondary Values - 5 cols */}
          <div className="lg:col-span-5 flex flex-col gap-6">
            {values
              .filter((v) => !v.featured)
              .map((val, idx) => {
                const Icon = val.icon;
                return (
                  <motion.div
                    key={val.title}
                    initial={{ opacity: 0, y: 24 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.5, delay: (idx + 1) * 0.1 }}
                    className="flex-1"
                  >
                    <DoubleBezelCard>
                      <div className="flex flex-col gap-4 h-full justify-between">
                        <div className="w-11 h-11 bg-brand-blue-50 text-brand-blue rounded-xl flex items-center justify-center border border-brand-blue-100 shrink-0">
                          <Icon className="h-5 w-5 text-brand-blue" />
                        </div>

                        <div className="space-y-1.5">
                          <h3 className="text-xl sm:text-2xl font-display uppercase tracking-tight text-brand-ink leading-tight">
                            {val.title}
                          </h3>
                          <p className="text-xs sm:text-sm text-brand-ink leading-relaxed font-sans">
                            {val.desc}
                          </p>
                        </div>
                      </div>
                    </DoubleBezelCard>
                  </motion.div>
                );
              })}
          </div>

        </div>

      </div>
    </section>
  );
}

```

### Componente: `src/components/nosotros/sobre-nosotros/AboutTimeline.tsx`

```tsx
'use client';

import React from 'react';
import { motion } from 'motion/react';
import { Compass, TrendingUp, Award, CheckCircle, Truck, MapPin } from 'lucide-react';
import DoubleBezelCard from '@/components/ui/DoubleBezelCard';

export default function AboutTimeline() {
  const milestones = [
    {
      year: '2019',
      title: 'Lanzamiento Inicial en MDQ',
      desc: 'Iniciamos operaciones con flota propia de motocicletas en las calles céntricas de Mar del Plata, apostando a un servicio ágil y de confianza.',
      icon: Compass,
    },
    {
      year: '2021',
      title: 'Soluciones PyME y LowCost',
      desc: 'Lanzamos la modalidad LowCost agrupada y el Plan Emprendedores para impulsar las ventas online durante la expansión del e-commerce local.',
      icon: TrendingUp,
    },
    {
      year: '2023',
      title: 'Consolidación de Flota Propia',
      desc: 'Estructura propia de repartidores uniformados y coordinados por WhatsApp para garantizar entregas puntuales sin tercerización.',
      icon: Truck,
    },
    {
      year: '2024',
      title: 'Pioneros MercadoLibre Flex en MDQ',
      desc: 'Nos convertimos en el socio logístico de referencia para entregas Same-Day de Mercado Libre en todo Mar del Plata.',
      icon: CheckCircle,
    },
    {
      year: '2025',
      title: 'Hub Logístico Friuli 1972',
      desc: 'Inauguración de nuestro depósito central en Chauvín con depósitos de paquetería, picking y tecnología de ruteo optimizado.',
      icon: MapPin,
    },
    {
      year: '2026',
      title: 'Infraestructura 3PL en todo Mar del Plata',
      desc: 'Más de 7 años de trayectoria consolidada con flota propia, cotizadores en tiempo real y fulfillment integral para tiendas online.',
      icon: Award,
    },
  ];

  return (
    <section
      id="about-timeline"
      className="py-20 sm:py-24 bg-brand-blue-50 relative overflow-hidden border-t border-brand-blue-100"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        {/* Header Block */}
        <div className="text-center max-w-2xl mx-auto mb-16 space-y-3.5">
          <span className="px-4 py-1.5 bg-brand-yellow text-brand-blue rounded-full text-xs sm:text-sm font-subheading uppercase tracking-widest inline-block font-bold transform -rotate-1 shadow-glow-yellow">
            TRAYECTORIA & EVOLUCIÓN
          </span>
          <h2 className="text-brand-ink text-3xl sm:text-5xl lg:text-6xl font-display uppercase tracking-tight leading-[1.05]">
            NUESTRA HISTORIA
          </h2>
          <p className="text-brand-ink font-sans text-sm sm:text-base max-w-lg mx-auto leading-relaxed">
            Más de 7 años transformando la última milla y la mensajería urbana en la ciudad de Mar del Plata.
          </p>
        </div>

        {/* Timeline body */}
        <div className="relative max-w-4xl mx-auto">
          {/* Central Vertical Stepper Line (brand-blue background, brand-blue-400 active bar) */}
          <div className="absolute left-6 md:left-1/2 md:-translate-x-1/2 top-4 bottom-4 w-1 bg-brand-blue hidden sm:block rounded-full">
            <div className="w-full h-full bg-brand-blue-400 rounded-full" />
          </div>

          <div className="space-y-8 sm:space-y-12">
            {milestones.map((milestone, idx) => {
              const Icon = milestone.icon;
              const isEven = idx % 2 === 0;

              return (
                <div
                  key={`${milestone.year}-${milestone.title}`}
                  className={`relative flex flex-col sm:flex-row items-start sm:items-center sm:justify-between gap-4 ${
                    isEven ? 'sm:flex-row-reverse' : ''
                  }`}
                >
                  {/* Concentric Node Circle in Yellow brand-yellow with White Ring */}
                  <div className="hidden sm:flex absolute left-6 md:left-1/2 md:-translate-x-1/2 w-10 h-10 rounded-full bg-brand-yellow border-2 border-brand-white ring-2 ring-brand-blue shadow-md items-center justify-center z-10 text-brand-blue">
                    <Icon className="h-4.5 w-4.5" />
                  </div>

                  {/* Spacer Column for Desktop */}
                  <div className="w-full sm:w-[45%] hidden sm:block" />

                  {/* Card Content Column - Double Bezel */}
                  <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    whileInView={{ opacity: 1, y: 0 }}
                    viewport={{ once: true }}
                    transition={{ duration: 0.45 }}
                    className="w-full sm:w-[45%]"
                  >
                    <DoubleBezelCard>
                      <div className="flex flex-col space-y-2">
                        <div className="flex items-center justify-between">
                          <span className="font-mono text-3xl sm:text-4xl text-brand-ink font-bold leading-none tabular-nums">
                            {milestone.year}
                          </span>
                          <span className="px-2.5 py-0.5 rounded-md bg-brand-yellow/20 text-2xs font-mono text-brand-blue font-bold uppercase border border-brand-yellow/40 transform -rotate-1 tabular-nums">
                            Hito MDQ
                          </span>
                        </div>
                        <h3 className="text-xl sm:text-2xl font-display uppercase tracking-tight text-brand-ink leading-tight">
                          {milestone.title}
                        </h3>
                        <p className="text-xs sm:text-sm text-brand-ink leading-relaxed font-sans">
                          {milestone.desc}
                        </p>
                      </div>
                    </DoubleBezelCard>
                  </motion.div>
                </div>
              );
            })}
          </div>
        </div>
      </div>
    </section>
  );
}

```

### Componente: `src/components/nosotros/sobre-nosotros/AboutTeam.tsx`

```tsx
'use client';

import React from 'react';
import { motion } from 'motion/react';
import { Users2, ShieldCheck, HeartHandshake, MapPin } from 'lucide-react';
import Image from 'next/image';
import DoubleBezelCard from '@/components/ui/DoubleBezelCard';

export default function AboutTeam() {
  const teamStats = [
    {
      number: '+20',
      role: 'Repartidores en Calle',
      desc: 'Cadetes capacitados y uniformados que conocen cada atajo y zona de Mar del Plata para entregas veloces y seguras.',
      icon: Users2,
      tag: 'Flota Propia',
    },
    {
      number: '100%',
      role: 'Base Operativa en MDQ',
      desc: 'Depósito central en Friuli 1972 para recepción, almacenamiento, consolidación de paquetes y despacho diario.',
      icon: MapPin,
      tag: 'Hub Chauvín',
    },
    {
      number: '< 2h',
      role: 'Tiempo Promedio Express',
      desc: 'Servicio prioritario punto a punto dentro del ejido urbano con monitoreo continuo de ruta.',
      icon: ShieldCheck,
      tag: 'Máxima Velocidad',
    },
    {
      number: '+7',
      role: 'Años de Trayectoria',
      desc: 'Compromiso ininterrumpido con comerciantes, emprendedores y empresas marplatenses.',
      icon: HeartHandshake,
      tag: 'Confianza Local',
    },
  ];

  return (
    <section
      id="about-team"
      className="py-20 sm:py-24 bg-brand-blue text-white relative z-10 overflow-hidden border-t border-white/10"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
        
        {/* Header Block */}
        <div className="text-left max-w-3xl mb-16 space-y-3.5">
          <span className="px-4 py-1.5 bg-brand-yellow text-brand-blue rounded-full text-xs sm:text-sm font-subheading uppercase tracking-widest inline-block font-bold transform -rotate-1 shadow-glow-yellow">
            FUERZA OPERATIVA & EXPERIENCIA
          </span>
          <h2 className="text-white text-3xl sm:text-5xl lg:text-6xl font-display uppercase tracking-tight leading-[1.05]">
            NUESTRO EQUIPO EN CALLE
          </h2>
          <p className="text-white/90 font-sans text-base sm:text-lg max-w-prose leading-relaxed">
            Una estructura humana consolidada con base física en la ciudad, lista para responder al ritmo de tu negocio.
          </p>
        </div>

        {/* Team Stats Grid */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {teamStats.map((stat, idx) => {
            const Icon = stat.icon;
            return (
              <motion.div
                key={stat.role}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                viewport={{ once: true }}
                transition={{ duration: 0.45, delay: idx * 0.08 }}
              >
                <DoubleBezelCard>
                  <div className="flex flex-col justify-between h-full space-y-5 relative overflow-hidden">
                    <Icon className="absolute -right-4 -bottom-4 w-28 h-28 text-brand-blue/5 pointer-events-none" />

                    <div>
                      <div className="flex items-center justify-between mb-3">
                        <div className="w-10 h-10 bg-brand-blue-50 text-brand-blue rounded-xl flex items-center justify-center border border-brand-blue-100">
                          <Icon className="w-5 h-5 text-brand-blue" />
                        </div>
                        <span className="text-2xs font-subheading uppercase tracking-wider bg-brand-yellow text-brand-blue px-2.5 py-0.5 rounded-full font-bold transform -rotate-1">
                          {stat.tag}
                        </span>
                      </div>

                      <span className="block font-mono text-5xl sm:text-6xl font-bold text-brand-ink leading-none mb-2 tabular-nums">
                        {stat.number}
                      </span>

                      <h3 className="text-xl font-display uppercase tracking-tight text-brand-ink leading-tight mb-2">
                        {stat.role}
                      </h3>

                      <p className="text-xs sm:text-sm text-brand-ink leading-relaxed font-sans">
                        {stat.desc}
                      </p>
                    </div>

                    <div className="pt-4 border-t border-brand-blue-100 flex items-center justify-between text-xs text-brand-ink font-mono">
                      <span className="flex items-center gap-1.5">
                        <Image src="/logo-envios-simplified.webp" alt="Envíos DosRuedas" width={16} height={16} className="object-contain" />
                        Envíos DosRuedas
                      </span>
                      <span className="font-bold text-brand-blue tabular-nums">MDQ 2026</span>
                    </div>
                  </div>
                </DoubleBezelCard>
              </motion.div>
            );
          })}
        </div>

      </div>
    </section>
  );
}

```

### Componente: `src/components/nosotros/sobre-nosotros/AboutMissionVision.tsx`

```tsx
'use client';

import React from 'react';
import { motion } from 'motion/react';
import { Target, Eye, Rocket, ShieldCheck } from 'lucide-react';
import DoubleBezelCard from '@/components/ui/DoubleBezelCard';
import CTANestedPill from '@/components/ui/CTANestedPill';

export default function AboutMissionVision() {
  return (
    <section
      id="about-mission-vision"
      className="py-20 sm:py-24 bg-brand-blue-50 relative overflow-hidden border-t border-brand-blue-100"
    >
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">

        {/* Header Block */}
        <div className="text-center max-w-2xl mx-auto mb-16 space-y-3.5">
          <span className="px-4 py-1.5 bg-brand-yellow text-brand-blue rounded-full text-xs sm:text-sm font-subheading uppercase tracking-widest inline-block font-bold transform -rotate-1 shadow-glow-yellow">
            PROPÓSITO & FUTURO
          </span>
          <h2 className="text-brand-ink text-3xl sm:text-5xl lg:text-6xl font-display uppercase tracking-tight leading-[1.05]">
            MISIÓN, VISIÓN & COMPROMISO
          </h2>
          <p className="text-brand-ink font-sans text-sm sm:text-base max-w-lg mx-auto leading-relaxed">
            Hacia dónde vamos y cuáles son las convicciones que guían cada entrega y ruteo diario en Mar del Plata.
          </p>
        </div>

        {/* Asymmetric Bento Grid */}
        <div className="grid grid-cols-1 lg:grid-cols-12 gap-6 lg:gap-8">

          {/* Card 1: Nuestra Misión (7 cols) */}
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5 }}
            className="lg:col-span-7"
          >
            <DoubleBezelCard>
              <div className="space-y-4 flex flex-col justify-between h-full">
                <div className="space-y-4">
                  <div className="w-12 h-12 bg-brand-blue-50 text-brand-blue rounded-2xl flex items-center justify-center border border-brand-blue-100">
                    <Target className="h-6 w-6 text-brand-blue" />
                  </div>

                  <h3 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-brand-ink leading-tight">
                    NUESTRA MISIÓN
                  </h3>

                  <p className="text-sm sm:text-base text-brand-ink leading-relaxed font-sans">
                    Brindar a cada negocio, e-commerce y particular de Mar del Plata una infraestructura de última milla confiable, accesible y ágil. Eliminamos las fricciones logísticas para que nuestros clientes puedan enfocarse en vender más y crecer.
                  </p>
                </div>

                <div className="pt-4 border-t border-brand-blue-100 flex items-center gap-2 text-xs font-subheading font-bold uppercase tracking-wider text-brand-ink">
                  <ShieldCheck className="h-4 w-4 text-brand-blue" />
                  <span>COMPROMISO OPERATIVO PERMANENTE</span>
                </div>
              </div>
            </DoubleBezelCard>
          </motion.div>

          {/* Card 2: Nuestra Visión (5 cols) */}
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: 0.1 }}
            className="lg:col-span-5"
          >
            <DoubleBezelCard>
              <div className="space-y-4 flex flex-col justify-between h-full">
                <div className="space-y-4">
                  <div className="w-12 h-12 bg-brand-yellow-50 text-brand-blue rounded-2xl flex items-center justify-center border border-brand-yellow-100">
                    <Eye className="h-6 w-6 text-brand-blue" />
                  </div>

                  <h3 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-brand-ink leading-tight">
                    NUESTRA VISIÓN
                  </h3>

                  <p className="text-sm sm:text-base text-brand-ink leading-relaxed font-sans">
                    Ser el estándar indiscutido de logística urbana y fulfillment 3PL en la Costa Atlántica, reconocidos por nuestra puntualidad, tecnología de ruteo y calidez en la atención humana.
                  </p>
                </div>

                <div className="pt-4 border-t border-brand-blue-100 flex items-center gap-2 text-xs font-subheading font-bold uppercase tracking-wider text-brand-ink">
                  <ShieldCheck className="h-4 w-4 text-brand-blue" />
                  <span>VISIÓN DE FUTURO 2026</span>
                </div>
              </div>
            </DoubleBezelCard>
          </motion.div>

          {/* Card 3: Compromiso e Innovación CTA (12 cols) */}
          <motion.div
            initial={{ opacity: 0, y: 24 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.5, delay: 0.2 }}
            className="lg:col-span-12"
          >
            <DoubleBezelCard>
              <div className="bg-brand-blue p-6 sm:p-8 rounded-[20px] border border-white/20 shadow-sm flex flex-col md:flex-row md:items-center justify-between gap-6 text-white">
                <div className="space-y-3 max-w-3xl">
                  <div className="flex items-center gap-3">
                    <div className="p-2.5 bg-white/10 text-brand-yellow rounded-xl border border-white/20">
                      <Rocket className="h-6 w-6 text-brand-yellow" />
                    </div>
                    <h3 className="text-2xl sm:text-3xl font-display uppercase tracking-tight text-white leading-none">
                      ¿LISTO PARA ENVIAR CON LOS MEJORES?
                    </h3>
                  </div>
                  <p className="text-sm sm:text-base text-white/90 leading-relaxed font-sans">
                    Sumate a las cientos de tiendas y emprendimientos de Mar del Plata que confían su logística diaria en Envíos DosRuedas. Cotizá en línea o hablá hoy con un asesor comercial.
                  </p>
                </div>

                <div className="shrink-0 flex flex-wrap items-center gap-3">
                  <CTANestedPill
                    href="/cotizar"
                    variant="primary"
                  >
                    Cotizar Envío
                  </CTANestedPill>
                  <CTANestedPill
                    href="/contacto"
                    variant="outline"
                  >
                    Contactar Asesor
                  </CTANestedPill>
                </div>
              </div>
            </DoubleBezelCard>
          </motion.div>

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

